#import mariadb
from dao.dummy_data import team_dummy_data, tid_count, soccer_team_avg_dummy_data
from team.team import Team
from soccerTeam.TeamStatisticFactory import TeamStatisticDAOFactory
from manager.managerRepository import ManagerDAO
from soccerTeam.soccerTeamDAO import SoccerTeamDAO
from soccerTeam.soccerTeamStatistics import SoccerTeam
from handler import utils
from Records.recordsDAO import RecordsDAO

class TeamRepository:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) ORDER BY team_name"
        cursor.execute(query)
        result = cursor.fetchall()
        team_tup = [team for team in result]
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj

    def get(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team.id = ?"
        cursor.execute(query, (tid,))
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao =  TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        return team_obj

    def add(self, team, username):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "INSERT INTO team(team_name, info) values(?, ?)"
        cursor.execute(query, (team.team_name, team.team_info,))
        teamid = cursor.lastrowid
        query2 = "SELECT id FROM sport WHERE sportname = ?"
        cursor.execute(query2, (team.sport_name,))
        sportid = cursor.fetchone()[0]
        query3 = "INSERT INTO team_sport(team_id, sport_id) values(?, ?)"
        cursor.execute(query3, (teamid, sportid,))
        team_obj = self.get(teamid)
        cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
        userId = cursor.fetchone()[0]
        cursor.execute("insert into manages(user_id, team_id) values (?,?)", (userId, team_obj[0].team_id,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return team_obj

    def edit(self, team):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "UPDATE team SET team_name = ?, info = ? WHERE id = ?"
        cursor.execute(query, (team.team_name, team.team_info, team.team_id,))
        query2 = "SELECT id FROM sport WHERE sportname = ?"
        cursor.execute(query2, (team.sport_name,))
        sportid = cursor.fetchone()[0]
        query3 = "UPDATE team_sport SET team_id = ?, sport_id = ? WHERE team_id = ?"
        cursor.execute(query3, (team.team_id, sportid, team.team_id,))
        self.conn.commit()
        team_obj = self.get(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj


    def delete(self, tid):
        self.conn = utils.connectDB()
        team_obj = self.get(tid)
        cursor = self.conn.cursor()
        query1 = "DELETE FROM team_sport WHERE team_id = ?"
        cursor.execute(query1, (tid,))
        query3 = "DELETE FROM manages WHERE id = (SELECT id FROM manages WHERE team_id = ?)"
        cursor.execute(query3, (tid,))
        query3 = "DELETE FROM team WHERE id = ?"
        cursor.execute(query3, (tid,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return team_obj

    def getBySport(self, sport_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE sportname = ? ORDER BY team_name"
        cursor.execute(query, (sport_name,))
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj

    def getByName(self, team_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team_name = ? ORDER BY sportname"
        cursor.execute(query, (team_name,))
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj

    def getByNameAndSport(self, team_name, sport_name):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE team_name = ? AND sportname = ?"
        cursor.execute(query, (team_name, sport_name,))
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj

    def getByManager(self, username):
        cursor = self.conn.cursor()
        query = "SELECT team.id, team_name, info, sportname FROM ((((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) join manages on team.id = manages.team_id) join user on user_id = user.id) where username = ?"
        cursor.execute(query, (username,))
        team_tup = cursor.fetchall()
        team_obj = [Team(team[0], team[1], team[2], team[3]) for team in team_tup]
        for team in team_obj:
            dao = TeamStatisticDAOFactory().getDAO(team.sport_name)
            team.sportStatistic = dao.getByTeamid(team.team_id)
            team.managers = ManagerDAO().getByTeamID(team.team_id)
            team.teamRecords = RecordsDAO().getByTeamID(team.team_id)
        cursor.close()
        self.conn.close()
        return team_obj 

    def getAvgStats(self, tid):
        return next(avg_stat[1:] for avg_stat in SoccerTeamDAO.getByid(tid))