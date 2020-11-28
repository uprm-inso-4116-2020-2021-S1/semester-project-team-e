from dao.dummy_data import users_dummy_data, uid_count, manages
from manager.manager import Manager
from handler import utils


class ManagerDAO:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT id, username, password, full_name, email FROM user"
        cursor.execute(query)
        result = cursor.fetchall()
        manager_tupl = [manager for manager in result]
        manager_obj = [Manager(manager[0], manager[1], manager[2], manager[3], manager[4]) for manager in manager_tupl]
        cursor.close()
        self.conn.close()
        return manager_obj

    def get(self, userid):
        cursor = self.conn.cursor()
        query = "SELECT id, username, password, full_name, email FROM user WHERE id = ?"
        cursor.execute(query, (userid,))
        manager = cursor.fetchone()
        cursor.close()
        return Manager(manager[0], manager[1], manager[2], manager[3], manager[4])


    def getByUsername(self, username):
        cursor = self.conn.cursor()
        query = "SELECT user.id, username, password, full_name, email FROM user WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        if result:
            managers = [Manager(manager[0], manager[1], manager[2], manager[3], manager[4]) for manager in result]
            return managers[0]
        else:
            return None


    def getByTeamID(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT user.id, username, password, full_name, email FROM (user JOIN manages ON user.id = user_id) WHERE team_id = ? ORDER BY full_name"
        cursor.execute(query, (tid,))
        result = cursor.fetchall()
        managers = [Manager(manager[0], manager[1], manager[2], manager[3], manager[4]) for manager in result]
        cursor.close()
        self.conn.close()
        return managers

    def add(self, manager):
        cursor = self.conn.cursor()
        query = "INSERT INTO user(username, password, full_name, email) VALUES(?, ?, ?, ?)"
        cursor.execute(query, (manager.username, manager.password, manager.full_name, manager.email,))
        managerid = cursor.lastrowid
        result = self.get(managerid)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result

    def delete(self, user_id):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        result = self.get(user_id)
        query = "DELETE FROM user WHERE id = ?"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result

    def edit(self, manager):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "UPDATE user SET email = %s, full_name = %s;"
        cursor.execute(query, (manager.email, manager.full_name))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return

