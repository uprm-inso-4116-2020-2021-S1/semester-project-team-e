class Manager:
    def __init__(self, user_id, team_id, username, password, full_name, email):
        self.user_id = user_id
        self.team_id = team_id
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name

    def serialize(self):
        return {'username' : self.username,
                'team_id' : self.team_id,
                'email' : self.email,
                'full_name' : self.full_name
                }

