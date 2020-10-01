from dao.dummy_data import users_dummy_data

class UserDAO:
    def get(self, username):
        return [ user for user in users_dummy_data if user[1] == username ][0]

    def add(self):
        pass