import requests
from datetime import datetime


class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals + assists

    def get_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:21}{self.team} {self.goals:2} + {self.assists:2} = {self.get_points()}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        json_players = requests.get(self.url).json()
        players = [f"{datetime.now()}\n"]
        for player_dict in json_players:
            player = Player(
                player_dict["name"],
                player_dict["nationality"],
                player_dict["team"],
                player_dict["goals"],
                player_dict["assists"],
            )
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_scorers = [f"Players from {nationality} {self.players[0]}"]
        players_from_nation = [
            player for player in self.players[1:] if player.nationality == nationality
        ]
        top_scorers += sorted(
            players_from_nation, key=lambda player: player.get_points(), reverse=True
        )
        return top_scorers
