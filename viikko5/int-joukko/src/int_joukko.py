from __future__ import annotations


class IntJoukko:
    def __init__(self, lukujono=None, unused_arg=None):
        self.lukujono = lukujono

    @property
    def lukujono(self):
        return self._lukujono

    @lukujono.setter
    def lukujono(self, new_lukujono):
        if isinstance(new_lukujono, set):
            self._lukujono = new_lukujono
        else:
            self._lukujono = set()

    def kuuluu(self, num: int) -> bool:
        return num in self.lukujono

    def lisaa(self, num: int):
        if not self.kuuluu(num):
            self.lukujono.add(num)

    def poista(self, num: int):
        if self.kuuluu(num):
            self.lukujono.remove(num)

    def mahtavuus(self) -> int:
        return len(self.lukujono)

    def to_int_list(self) -> list:
        return list(self.lukujono)

    @staticmethod
    def yhdiste(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        return IntJoukko(a.lukujono.union(b.lukujono))

    @staticmethod
    def leikkaus(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        return IntJoukko(a.lukujono.intersection(b.lukujono))

    @staticmethod
    def erotus(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        return IntJoukko(a.lukujono.difference(b.lukujono))

    def __str__(self):
        return "{" + f'{", ".join(str(num) for num in self.lukujono)}' + "}"
