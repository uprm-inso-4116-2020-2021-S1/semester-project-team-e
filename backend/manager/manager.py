class Manager:
    def __init__(self, manager_id, email, username, password, full_name):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name

    def serialize(self):
        return {'username' : self.username,
                'email' : self.email,
                'full_name' : self.full_name
                }

