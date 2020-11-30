from soccerTeam.soccerTeamDAO import SoccerTeamDAO
from team.team import Team

class SoccerTeamSpecification:

    def isValidTeam(self, Team):
        players = SoccerTeamDAO().getByTeamid(Team.team_id)
        count = 0
        for x in players:
            count += 1
        if count >= 1:
            return True
        else:
            return False