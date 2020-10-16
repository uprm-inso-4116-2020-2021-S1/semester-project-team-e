from dao.dummy_data import users_dummy_data, uid_count
from manager.manager import Manager

class ManagerDAO:
    def get(self, username):
        # TODO: Connect to database and make query 
        manager = [ user for user in users_dummy_data if user[1] == username ][0]
        return Manager(manager[0], manager[1], manager[2], manager[3])

    # def getByTeamID(self, tid):
        #  manager = [ user for user in users_dummy_data if user[2] == tid ][0]

    def add(self, manager):
        # TODO: Connect to database and make query
         newTeam = Manager(uid_count, manager.username, manager.email, manager.password)
         return newTeam