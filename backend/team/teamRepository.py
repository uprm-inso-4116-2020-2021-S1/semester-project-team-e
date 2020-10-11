#import mariadb
from dao.dummy_data import team_dummy_data, tid_count
from team.team import Team
from soccerTeam.soccerTeamDAO import SoccerTeamDAO
from soccerTeam.soccerTeamStatistics import SoccerTeam

class TeamRepository:
    def __init__(self):
        # self.conn = generic_db_connect()
        pass

    def getAll(self):
        # TODO: Connect to database and make query
        team = [team for team in team_dummy_data][0]
        teamStats = SoccerTeamDAO().getAll()
        count = 0
        for team in team:
            for newTeamStats in teamStats:
                if newTeamStats[1] == SoccerTeamDAO.getByid(team[0]):
                    team.push(teamStats[count])
                count += 1
        return  [ Team(team[0], team[1], team[2], team[3]) for team in team_dummy_data ]

    def get(self, tid):
        # TODO: Connect to database and make query
        team = [ team for team in team_dummy_data if team[0] == tid ][0]
        team.push(SoccerTeamDAO().getByTeamid(tid))
        return Team(team[0], team[1], team[2], team[3])

    def add(self, team):
        # TODO: Connect to database and make query
        newTeam = Team(tid_count, team.team_name, team.team_info, team.sport_name)
        # team_dummy_data.append(newTeam)
        # tid_count += 1
        return newTeam 

    def edit(self, team):
        # TODO: Connect to database and make query
        newTeam = Team(tid_count, team.team_name, team.team_info, team.sport_name)
        return newTeam

    def delete(self, tid):
        # TODO: Connect to database and make query
        team = [ team for team in team_dummy_data if team[0] == tid ][0]
        return Team(team[0], team[1], team[2], team[3])

    def getBySport(self, sport_name):
        # TODO: Connect to database and make query
        teams = [ team for team in team_dummy_data if team[3] == sport_name]
        teamStats = SoccerTeamDAO().getAll()
        count = 0
        for teams in teams:
            for newTeamStats in teamStats:
                if newTeamStats[1] == SoccerTeamDAO.getByid(teams[0]):
                    teams.push(teamStats[count])
                count += 1
        return [ Team(team[0], team[1], team[2], team[3]) for team in teams ]

    def getByName(self, team_name):
        # TODO: Connect to database and make query
        teams = [ team for team in team_dummy_data if team[1] == team_name]
        teamStats = SoccerTeamDAO().getAll()
        count = 0
        for teams in teams:
            for newTeamStats in teamStats:
                if newTeamStats[1] == SoccerTeamDAO.getByid(teams[0]):
                    teams.push(teamStats[count])
                count += 1
        return [ Team(team[0], team[1], team[2], team[3]) for team in teams ]

    def getByNameAndSport(self, team_name, sport_name):
        # TODO: Connect to database and make query
        teams = [ team for team in team_dummy_data if (team[3] == sport_name and team[1] == team_name) ]
        teamStats = SoccerTeamDAO().getAll()
        count = 0
        for teams in teams:
            for newTeamStats in teamStats:
                if newTeamStats[1] == SoccerTeamDAO.getByid(teams[0]):
                    teams.push(teamStats[count])
                count += 1
        return [ Team(team[0], team[1], team[2], team[3]) for team in teams ]