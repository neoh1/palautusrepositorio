class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.players = {player1_name: 0, player2_name: 0}
        self.p1 = player1_name
        self.p2 = player2_name

    def won_point(self, player_name: str):
        self.players[player_name] += 1

    def calls_equal(self, num: int) -> str:
        calls = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Forty-All"}
        if num in calls:
            return calls[num]
        return "Deuce"

    def calls_four_points_more(self, num: int) -> str:
        if num > 2: num = 2
        if num < -2: num = -2
        calls = {1: "Advantage player1", -1: "Advantage player2",
                 2 : "Win for player1",  -2: "Win for player2"}
        return calls[num]

    def calls_midgame(self, num1: int, num2: int) -> str:
        calls = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return calls[num1]+"-"+calls[num2]

    def get_score(self):
        score = ""
        p1_score = self.players[self.p1]
        p2_score = self.players[self.p2]
        if p1_score == p2_score:
            score = self.calls_equal(p1_score)
        elif p1_score >= 4 or p2_score >= 4:
            score = self.calls_four_points_more(p1_score - p2_score)
        else:
            score = self.calls_midgame(p1_score, p2_score)
        return score
