from dao.dummy_data import users_dummy_data, uid_count

class UserDAO:
    def get(self, username):
        # TODO: Connect to database and make query 
        return [ user for user in users_dummy_data if user[1] == username ][0]

    def add(self, json):
        # TODO: Connect to database and make query
         newTeam = (uid_count, json['username'], json['email'])
         return newTeam