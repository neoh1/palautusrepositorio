import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.mehu = Tuote("Mehu", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_eri_lisaysta_jalkeen_korin_hinta_on_lisaysten_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        for _ in range(2):
            self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_lisaamisen_jalkeen_kori_hinta_on_kaksi_kertaa_tuote(self):
        for _ in range(2):
            self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisays_koriin_ostos_tuotteen_nimella_ja_lukumaaralla(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        for _ in range(2):
            self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_lisaamisen_jalkeen_korissa_ostoksen_nimi_lkm_kaksi(self):
        for _ in range(2):
            self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_korissa_kaksi_samaa_yksi_poistetaan_koriin_yksi_ostos_yksi_kpl(self):
        for _ in range(2):
            self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_koriin_lisataan_tuote_ja_poistetaan_kori_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_kori(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()), 0)
