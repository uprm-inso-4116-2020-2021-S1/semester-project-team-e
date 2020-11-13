from dao.dummy_data import users_dummy_data, uid_count, manages
from manager.manager import Manager
from handler import utils

class ManagerDAO:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        return

    def get(self, username):
        cursor = self.conn.cursor()
        query = "SELECT username, full_name, email FROM user WHERE username = %s"
        cursor.execute(query, [username])
        manager = cursor.fetchone()
        return Manager(manager[0], manager[1], manager[2], manager[3], manager[4])

    def getByTeamID(self, tid):
        cursor = self.conn.cursor()
        query = "SELECT team.id, username, email, password, full_name FROM ((user JOIN manages ON user.id = user_id) JOIN team ON team_id = team.id) WHERE team.id = %s ORDER BY full_name;"
        cursor.execute(query, [tid])
        result = cursor.fetchall()
        managers = [ Manager(manager[0], manager[1], manager[2], manager[3], manager[4]) for manager in result]
        return managers

    def delete(self, user_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM user WHERE id = %s;"
        cursor.execute(query, (user_id))
        return

    def edit(self, user_id, manager):
        cursor = self.conn.cursor()
        query = "UPDATE user SET email = %s, full_name = %s;"
        cursor.execute(query, (manager.email, manager.full_name))
        return

