import requests
from player import Player
from datetime import datetime
"""
Tee ohjelma, joka listaa suomalaisten pelaajien tilastot. 
"""
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []
    nationality = 'FIN'
    for player_dict in response:
        if player_dict['nationality'] == nationality:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )
            players.append(player)

    print(f"Players from {nationality} {datetime.now()}\n")
    for player in sorted(players, key=lambda player: player.points, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
