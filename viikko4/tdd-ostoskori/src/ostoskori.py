from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for _, ostos in self._ostokset.items())

    def hinta(self):
        return sum(ostos.hinta() for _, ostos in self._ostokset.items())

    def lisaa_tuote(self, lisattava: Tuote):
        try:
            self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)
        except KeyError:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        pnimi = poistettava.nimi()
        try:
            self._ostokset[pnimi].muuta_lukumaaraa(-1)
            if self._ostokset[pnimi].lukumaara() == 0:
                self._ostokset.pop(pnimi)
        except KeyError:
            print("Ei voida poistaa tuotetta, sitä ei ole ostoskorissa.")

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self):
        return [ostos for _, ostos in self._ostokset.items()]
