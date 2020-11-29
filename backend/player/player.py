class Player():
    def __init__(self, player_id, player_name, team_name, position, height, weight, sport_name):
        self.player_id = player_id
        self.player_name = player_name
        self.team_name = team_name
        self.position = position
        self.height = height
        self.weight = weight
        self.sport_name = sport_name



    def serialize(self):
        return {
            'player' : self.player_id,
            'player_name' : self.player_name,
            'team' : self.team_name,
            'position' : self.position,
            'height' : self.height,
            'weight' : self.weight,
            'sport' : self.sport_name
        }

    # CLASS_NAME = 'Player'
    # DATABASE_TABLE_NAME = 'player'
    #
    # PLAYER_DB_FORMAT = DB_Entity._get_column_names(DATABASE_TABLE_NAME)
    #
    # PLAYER_UPDATE_FORMAT = [
    #     'player_name',
    #     'height',
    #     'weight',
    #     'team_name',
    #     'sport_name',
    #     # 'team_sport_id',
    #     'player_id'
    # ]
    #
    # PLAYER_DB_ADD_FORMAT = [
    #     'player_name',
    #     'height',
    #     'weight',
    #     'team_name',
    #     'sport_name',
    # ]
    #
    #
    # def __init__(self, player_id=None, player_name=None, height=None, weight=None, team_name=None, sport_name=None, team_sport_id=None, sport_stats=None):
    #     self.player_id = player_id
    #     self.player_name = player_name
    #     self.height = height
    #     self.weight = weight
    #     self.team_name = team_name
    #     self.sport_name = sport_name
    #     self.team_sport_id = team_sport_id
    #     if isinstance(sport_stats, PlayerStatistic):
    #         self.player_sport_stats = sport_stats.__dict__
    #     else:
    #         self.player_sport_stats = sport_stats
    #
    # def to_db_format(self):
    #     db_dict = {}
    #     inst_values = vars(self)
    #     for entry in Player.PLAYER_DB_FORMAT:
    #         db_dict[entry] = inst_values[entry]
    #
    #     return db_dict
    #
    # def to_specified_db_format(self, format):
    #     db_dict = {}
    #     inst_values = vars(self)
    #     for entry in format:
    #         db_dict[entry] = inst_values[entry]
    #
    #     return db_dict
    #
    #
    # @staticmethod
    # def search_by_atr(recvd: dict):
    #     pass
    #
    #
    # @staticmethod
    # def search_by_atr(front_end_dict: dict):                                                     # This last bit with the dictionary could be eliminated later
    #     return Player.get_by_attribute(Player.PLAYER_DB_FORMAT, front_end_dict, Player.CLASS_NAME, {})