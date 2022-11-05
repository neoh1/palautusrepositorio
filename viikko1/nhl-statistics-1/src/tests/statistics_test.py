import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    
    def setUp(self):
        # offline testing using Stub
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_return_player(self):
        player_semenko = self.statistics.search("Semenko")
        self.assertEqual(str(player_semenko), "Semenko EDM 4 + 12 = 16", "Search did not return player correctly")

    def test_search_return_none(self):
        player_none = self.statistics.search("fdsfakj3234dsas")
        self.assertIsNone(player_none, "Search did not return None for test-name")

    def test_team_return(self):
        team_name = 'DET'
        team_members = self.statistics.team(team_name)
        self.assertEqual(str(team_members[0]), "Yzerman DET 42 + 56 = 98", 
                                               "Correct team members were not returned")

    def test_top_player(self):
        top_two = self.statistics.top(1)
        top_two = list(map(str, top_two))
        stub_top_two = ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99']
        self.assertCountEqual(top_two, stub_top_two, "Top player lists are not the same")

