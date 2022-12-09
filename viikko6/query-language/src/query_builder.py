from collections import deque
from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn


class QueryBuilder:
    def __init__(self, queries=All()):
        self.queries = queries

    def hasAtLeast(self, points: int, point_type: str):
        return QueryBuilder(And(self.queries, HasAtLeast(points, point_type)))

    def hasFewerThan(self, points: int, point_type: str):
        return QueryBuilder(And(self.queries, HasFewerThan(points, point_type)))

    def oneOf(self, queries1, queries2):
        return QueryBuilder(Or(queries1, queries2))

    def playsIn(self, team):
        return QueryBuilder(And(self.queries, PlaysIn(team)))

    def build(self):
        return self.queries
