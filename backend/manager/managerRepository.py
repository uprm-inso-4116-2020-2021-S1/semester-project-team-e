from dao.dummy_data import users_dummy_data, uid_count, manages
from manager.manager import Manager

class ManagerDAO:
    def get(self, username):
        # TODO: Connect to database and make query 
        manager = [ user for user in users_dummy_data if user[1] == username ][0]
        return Manager(manager[0], manager[1], manager[2], manager[3], manager[4])

    def getByTeamID(self, tid):
        manager_ids = [ manage[0] for manage in manages if manage[1] == tid]
        managers = [ Manager(manager[0], manager[1], manager[2], manager[3], manager[4]) for manager in users_dummy_data if (manager[0] in manager_ids) ]
        return managers

    def add(self, manager):
        # TODO: Connect to database and make query
         newTeam = Manager(uid_count, manager.username, manager.email, manager.password, manager.full_name)
         return newTeam