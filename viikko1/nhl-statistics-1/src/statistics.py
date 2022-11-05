from player_reader import PlayerReader


def sort_by_type(player, sorter=None):
    if not sorter:
        return player.points
    if sorter.value == 2:
        return player.goals
    elif sorter.value == 3:
        return player.assists
    return player.points


class Statistics():
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sorter=0):
        

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by_type(player, sorter)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
