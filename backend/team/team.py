class Team():
    def __init__(self, team_id, team_name, team_info, sport_name):
        self.team_id = team_id
        self.team_name = team_name
        self.team_info = team_info
        self.sport_name = sport_name
        self.sportStatistic = []
        self.teamRecords = []
        self.managers = []
        self.players = []
        self.playerStatistics = []


    def serialize(self):
        return {'team' : self.team_id,
                'team_name' : self.team_name,
                'team_info' : self.team_info,
                'sport_name' : self.sport_name,
                'team_statistics' : [ stat.__dict__ for stat in self.sportStatistic ],
                'team_Records': [records.__dict__ for records in self.teamRecords],
                'managers' : [ manager.serialize() for manager in self.managers ],
                'players' : [ player.serialize() for player in self.players],
                'player_statistics': [playerStat.__dict__ for playerStat in self.playerStatistics]
                }




