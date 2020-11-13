#import mariadb
from dao.dummy_data import team_dummy_data, tid_count, soccer_team_avg_dummy_data
from team.team import Team
from soccerTeam.TeamStatisticFactory import TeamStatisticDAOFactory
from manager.managerRepository import ManagerDAO
from soccerTeam.soccerTeamDAO import SoccerTeamDAO
from soccerTeam.soccerTeamStatistics import SoccerTeam
from handler import utils

class TeamRepository:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) ORDER BY team_name;"
        cursor.execute(query)
        result = cursor.fetchall()
        team_tup = [team for team in result]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
        return team_obj

    def get(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team.id = %s;"
        cursor.execute(query, [tid])
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
        return team_obj

    def add(self, team):
        cursor = self.conn.cursor()
        query = "INSERT INTO team(team_name, info) values(%s, %s) returning id;"
        teamid = cursor.execute(query, [team.team_name], [team.team_info])
        query2 = "SELECT id FROM sport WHERE sportname = %s;"
        sportid = cursor.execute(query2, [team.sport_name])
        query3 = "INSERT INTO team_sport(team_id, sport_id) values(%s, %s);"
        cursor.execute(query3, [teamid], [sportid])
        return teamid

    def edit(self, team):
        cursor = self.conn.cursor()
        query = "UPDATE team SET team_name = %s, info = %s;"
        cursor.execute(query, [team.team_name], [team.team_info])
        query2 = "SELECT id FROM sport WHERE sportname = %s;"
        sportid = cursor.execute(query2, [team.sport_name])
        query3 = "UPDATE team_sport SET team_id = %s, sport_id = %s;"
        cursor.execute(query3, [team.team_id], [sportid])
        return

    def delete(self, tid):
        cursor = self.conn.cursor()
        query = "DELETE FROM team WHERE id = %s;"
        cursor.execute(query, [tid])
        return

    def getBySport(self, sport_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE sportname = %s ORDER BY team_name;"
        cursor.execute(query, [sport_name])
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
        return team_obj

    def getByName(self, team_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team_name = %s ORDER BY sportname;"
        cursor.execute(query, [team_name])
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
        return team_obj

    def getByNameAndSport(self, team_name, sport_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team_name = %s AND sportname = %s;"
        cursor.execute(query, [team_name], [sport_name])
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
        return team_obj

    def getAvgStats(self, tid):
        return next(avg_stat[1:] for avg_stat in soccer_team_avg_dummy_data if avg_stat[0] == tid)