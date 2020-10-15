class Team():
    def __init__(self, team_id, team_name, team_info, sport_name):
        self.team_id = team_id
        self.team_name = team_name
        self.team_info = team_info
        self.sport_name = sport_name
        self.sportStatistic = []

    def serialize(self):
        return {'team' : self.team_id,
                'team_name' : self.team_name,
                'team_info' : self.team_info,
                'sport_name' : self.sport_name,
                'team_statistics' : [ stat.__dict__ for stat in self.sportStatistic ]
                }




