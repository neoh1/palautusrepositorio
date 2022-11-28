from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset =  {}


    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return sum(ostos.lukumaara() for _, ostos in self._ostokset.items())

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum(ostos.hinta() for _, ostos in self._ostokset.items())

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        try:
            self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)
        except KeyError:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pnimi = poistettava.nimi()
        try:
            self._ostokset[pnimi].muuta_lukumaaraa(-1)
            if self._ostokset[pnimi].lukumaara == 0:
                del self._ostokset[pnimi]
        except KeyError:
            print("Ei voida poistaa, tuotetta ei ole ostoskorissa")

    def tyhjenna(self):
        ...

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return [ostos for _, ostos in self._ostokset.items()]
