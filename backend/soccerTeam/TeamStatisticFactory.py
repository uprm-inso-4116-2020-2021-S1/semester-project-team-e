from soccerTeam.soccerTeamDAO import SoccerTeamDAO

class TeamStatisticDAOFactory:
    def getDAO(self, sport):
        if sport == 'soccer':
            return SoccerTeamDAO()
        else:
            pass