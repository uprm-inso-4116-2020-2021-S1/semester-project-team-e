import mariadb
from dao.dummy_data import team_dummy_data, tid_count

class TeamDAO:
    def __init__(self):
        # self.conn = generic_db_connect()
        pass

    def getAll(self):
        # TODO: Connect to database and make query
        return team_dummy_data

    def get(self, tid):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if team[0] == tid ]

    def add(self, json):
        # TODO: Connect to database and make query
        newTeam = (tid_count, json['team_name'], json['team_info'], json['sport_name'])
        # team_dummy_data.append(newTeam)
        # tid_count += 1
        return [ newTeam ]

    def edit(self, tid, json):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if team[0] == tid ]

    def delete(self, tid):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if team[0] != tid ]

    def getBySport(self, sport_name):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if team[3] == sport_name]

    def getByName(self, team_name):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if team[1] == team_name]

    def getByNameAndSport(self, team_name, sport_name):
        # TODO: Connect to database and make query
        return [ team for team in team_dummy_data if (team[3] == sport_name and team[1] == team_name) ]