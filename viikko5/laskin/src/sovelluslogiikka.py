class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = [tulos]

    def miinus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos -= arvo

    def plus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos += arvo

    def nollaa(self):
        self.edellinen.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = arvo

    def kumoa(self):
        if not self.edellinen:
            self.tulos = 0
        else:
            self.tulos = self.edellinen.pop()
