from player_statistics.playerStatistics import PlayerStatistic


class Player:
    
    PLAYER_DB_FORMAT = [        
        'player_id',
        'player_name',
        'height',
        'weight',
        'team_name',
        'sport_name',
        'team_sport_id',    
    ]    

    PLAYER_UPDATE_FORMAT = [
        'player_name',
        'height',
        'weight',
        'team_name',
        'sport_name',
        # 'team_sport_id',
        'player_id'
    ]

    PLAYER_DB_ADD_FORMAT = [        
        'player_name',
        'height',
        'weight',
        'team_name',
        'sport_name',        
    ]


    def __init__(self, player_id=None, player_name=None, height=None, weight=None, team_name=None, sport_name=None, team_sport_id=None, sport_stats=None):
        self.player_id = player_id
        self.player_name = player_name
        self.height = height
        self.weight = weight
        self.team_name = team_name
        self.sport_name = sport_name 
        self.team_sport_id = team_sport_id
        if isinstance(sport_stats, PlayerStatistic):
            self.player_sport_stats = sport_stats.__dict__
        else:
            self.player_sport_stats = sport_stats

    def to_db_format(self):
        db_dict = {}
        inst_values = vars(self)
        for entry in Player.PLAYER_DB_FORMAT:
            db_dict[entry] = inst_values[entry]

        return db_dict

    def to_specified_db_format(self, format):
        db_dict = {}
        inst_values = vars(self)
        for entry in format:
            db_dict[entry] = inst_values[entry]

        return db_dict