# -- FILE: features/steps/mopes_steps.py
from behave import given, when, then, step
from mopes import Game, Team, Player, Ball


@given(u'we have an empty game')
def step_impl(context):
    context.game = Game()


@given(u'we have team {team_id:d} with players {player1_name} and {player2_name}')
def step_impl(context, team_id, player1_name, player2_name):
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    if team_id == 1:
        context.team1 = Team(player1, player2)
    elif team_id == 2:
        context.team2 = Team(player1, player2)
    else:
        raise ValueError("team_id is not valid")


@when(u'we add the team {team_id:d} to the game')
def step_impl(context, team_id):
    if team_id == 1:
        context.game.set_team1(context.team1)
    elif team_id == 2:
        context.game.set_team2(context.team1)
    else:
        raise ValueError("team_id is not valid")


@then(u'the team {team_id:d} should have a score of {score:d} points')
def step_impl(context, team_id, score):
    if team_id == 1:
        assert context.game.score.team1 == score
    elif team_id == 2:
        assert context.game.score.team2 == score
    else:
        raise ValueError("team_id is not valid")


@given(u'we have an initialized game with two teams')
def step_impl(context):
    context.game = Game()
    players = []
    for i in range(1, 5):
        players.append(Player('player' + str(i)))
    team1 = Team(players[0], players[1])
    team2 = Team(players[2], players[3])
    context.game.set_team1(team1)
    context.game.set_team2(team2)


@given(u'the current ball color is {color}')
def step_impl(context, color):
    context.current_ball = color


@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
    if team_id == 1:
        context.game.goal_team1(context.current_ball)
    elif team_id == 2:
        context.game.goal_team2(context.current_ball)
    else:
        raise ValueError("team_id is not valid")


@given(u'the next sequence of score actions')
def step_impl(context):
    for row in context.table:
        color = row['ball']
        if row['team'] == 1:
            context.game.goal_team1(color)
        elif row['team'] == 2:
            context.game.goal_team2(color)
        else:
            raise ValueError("team_id is not valid")


@given(u'the team {team_id:d} has a score of {points:d} points')
def step_impl(context, team_id, points):
    raise NotImplementedError(u'STEP: Given the team 1 has a score of 9 points')


@then(u'the game is over')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the game is over')


@then(u'the winner team is the team 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the winner team is the team 1')


@when(u'the team 1 scores an autogoal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the team 1 scores an autogoal')

