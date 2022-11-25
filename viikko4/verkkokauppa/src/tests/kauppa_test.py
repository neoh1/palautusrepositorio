import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.kaupan_tili = "33333-44455"
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "mehu", 6)
            if tuote_id == 3:
                return Tuote(3, "cola", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        self.kauppa.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_koriin_tuote_jota_varastossa_suoritetaan_ostos(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kaupan_tili, 5
        )

    def test_koriin_kaksi_eri_tuotetta_joita_varastossa_suoritetaan_ostos(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kaupan_tili, 11
        )

    def test_koriin_tuote_varastossa_tuote_ei_varastossa_suorita_ostos(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)  # ei varastossa
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kaupan_tili, 5
        )

    def test_asiointi_nolla_hinnat(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", self.kaupan_tili, 6
        )

    def test_uusi_viite_jokaiselle_maksutapahtumalle(self):
        viitegen_mock = Mock(wraps=Viitegeneraattori())
        store = Kauppa(self.varasto_mock, self.pankki_mock, viitegen_mock)
        store.aloita_asiointi()
        store.lisaa_koriin(1)
        store.tilimaksu("pekka", "12345")
        self.assertEqual(viitegen_mock.uusi.call_count, 1)

        store.aloita_asiointi()
        store.lisaa_koriin(2)
        store.tilimaksu("esa", "11223")
        self.assertEqual(viitegen_mock.uusi.call_count, 2)

        store.aloita_asiointi()
        store.lisaa_koriin(1)
        store.tilimaksu("sami", "99999")
        self.assertEqual(viitegen_mock.uusi.call_count, 3)

    def test_poista_korista_palautuu_varastoon(self):
        varasto_mock = Mock(wraps=Varasto())
        store = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        store.aloita_asiointi()
        store.lisaa_koriin(1)
        store.poista_korista(1)
        self.assertEqual(varasto_mock.saldo(1), 100)
