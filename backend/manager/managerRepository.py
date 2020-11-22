from dao.dummy_data import users_dummy_data, uid_count, manages
from manager.manager import Manager
from handler import utils

class ManagerDAO:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT id, team_id, username, password, full_name, email FROM user"
        cursor.execute(query)
        result = cursor.fetchall()
        manager_tupl = [manager for manager in result]
        manager_obj = [Manager(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]) for manager in manager_tupl]
        return manager_obj

    def get(self, userid):
        cursor = self.conn.cursor()
        query = "SELECT id, team_id, username, password, full_name, email FROM user WHERE id = ?"
        cursor.execute(query, (userid,))
        manager = cursor.fetchone()
        return Manager(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5])

    def getByUsername(self, username):
        cursor = self.conn.cursor()
        query = "SELECT id, team_id, username, password, full_name, email FROM user WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        managers = [Manager(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]) for manager in result]
        return managers

    def getByTeamID(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT id, team_id, username, password, full_name, email FROM user WHERE team_id = ? ORDER BY full_name"
        cursor.execute(query, (tid,))
        result = cursor.fetchall()
        managers = [ Manager(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]) for manager in result]
        return managers

    def add(self, manager):
        cursor = self.conn.cursor()
        query = "INSERT INTO user(team_id, username, password, full_name, email) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(query, (manager.team_id, manager.username, manager.password, manager.full_name, manager.email,))
        managerid = cursor.lastrowid
        result = self.get(managerid)
        self.conn.commit()
        return result

    def delete(self, user_id):
        cursor = self.conn.cursor()
        result = self.get(user_id)
        query = "DELETE FROM user WHERE id = ?"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return result

    def edit(self, manager):
        cursor = self.conn.cursor()
        query = "UPDATE user SET email = ?, full_name = ?, team_id = ?"
        cursor.execute(query, (manager.email, manager.full_name, manager.team_id,))
        self.conn.commit()
        return

    # def addManagertoTeam(self, teamid, user):
    #     cursor = self.conn.cusror()
    #     query = "INSERT INTO manages(user_id, team_id) VALUES(?, ?)"
    #     cursor.execute(query, (user.user_id, teamid,))
    #     self.conn.commit()
    #     return user