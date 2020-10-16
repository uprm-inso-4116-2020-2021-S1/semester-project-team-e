#import mariadb
from dao.dummy_data import team_dummy_data, tid_count
from team.team import Team
from soccerTeam.TeamStatisticFactory import TeamStatisticDAOFactory

class TeamRepository:
    def __init__(self):
        pass

    def getAll(self):
        team_tup = [team for team in team_dummy_data]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
        return team_obj

    def get(self, tid):
        # TODO: Connect to database and make query
        team_tup = [ team for team in team_dummy_data if team[0] == tid ]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            # User DAO factory to get statistics???
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
        return team_obj

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
        return [ Team(team[0], team[1], team[2], team[3]) for team in teams ]

    def getByName(self, team_name):
        # TODO: Connect to database and make query
        team_tup = [ team for team in team_dummy_data if team[1] == team_name]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            # User DAO factory to get statistics???))
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
        return team_obj

    def getByNameAndSport(self, team_name, sport_name):
        # TODO: Connect to database and make query
        team_tup = [ team for team in team_dummy_data if (team[3] == sport_name and team[1] == team_name) ]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            # User DAO factory to get statistics???
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
        return team_obj