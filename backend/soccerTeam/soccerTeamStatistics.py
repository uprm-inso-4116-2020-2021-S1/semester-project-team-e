class SoccerTeam:
    def __init__(self, statid, team_id, wins, draw, losses, goals_for, goals_allowed, goal_difference, points, date):
        self.statid = statid
        self.team_id = team_id
        self.wins = wins
        self.draw = draw
        self.losses = losses
        self.goals_for = goals_for
        self.goals_allowed = goals_allowed
        self.goal_difference = goal_difference
        self.points = points
        self.date = date