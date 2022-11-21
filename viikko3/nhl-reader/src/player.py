class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals+assists

    
    def __str__(self):
        return f"{self.name:21}{self.team} {self.goals:2} + {self.assists:2} = {self.points}"
