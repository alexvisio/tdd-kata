class Score:
    def __init__(self):
        self.team1 = 0
        self.team2 = 0


class Game(object):
    ball_value_table = {
        'white': 1,
        'blue': 2,
        'yellow': -1
    }

    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.score = Score()

    def set_team1(self, team1):
        self.team1 = team1

    def set_team2(self, team2):
        self.team2 = team2

    def goal_team1(self, ball_color):
        score_value = self.ball_value_table[ball_color]
        self.score.team1 += score_value

    def goal_team2(self, ball_color):
        score_value = self.ball_value_table[ball_color]
        self.score.team2 += score_value


class Player(object):
    def __init__(self, player_name):
        self.name = player_name


class Team(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Ball(object):
    pass