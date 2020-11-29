from backend.player.playerDAO import PlayerDAO
from backend.team.team import Team

class SoccerTeamSpecification:

    def isValidTeam(self, Team):
        players = PlayerDAO().getByTeamID(Team.team_id)
        count = 0
        for x in players:
            count += 1
        if count >= 7:
            return True
        else:
            return False