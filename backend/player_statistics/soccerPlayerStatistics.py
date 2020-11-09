

from player_statistics.playerStatistics import PlayerStatistic

class SoccerPlayerStatistic(PlayerStatistic):

    CLASS_NAME = 'SoccerPlayerStatistic'

    ENTITY_TO_DB_MAPPING = {
        CLASS_NAME : 'soccer_individual_statistics',
        'date' : 'year',
    }

    SOCCER_PLAYER_STATISTIC_FORMAT = [
        'id',
        'player_id',
        # 'position', # no esta en db???
        'date',
        # 'halve_number',
        'saves',
        'goals_scored',
        'assists',
        'tackles_won',
        'passes_completed',
        'red_cards',
        'yellow_cards',
    ]
    

    SOCCER_PLAYER_STATISTIC_DB_FORMAT = [
        # TODO ver que vas a hacer con el nombre de date y year que aparecen distintos en el codigo y en la base de datos
    ]

    SOCCER_PLAYER_UPDATE_FORMAT = [

    ]
    
    # TODO cambiar el db para que el stat sea determinado solo con el player id y removerle el id
    def __init__(self, id = None, player_id=None, position=None, date=None, halve_number=None, gamesPlayed=None, saves=None, goalsScored=None, assists=None, tacklesWon=None, passes_completed=None, red_cards=None, yellow_cards=None):
        super(SoccerPlayerStatistic, self).__init__(player_id, position, date, gamesPlayed)                
        self.id = id
        self.halve_number = halve_number
        self.saves = saves
        self.goalsScored = goalsScored
        self.assists = assists
        self.tacklesWon = tacklesWon
        self.passes_completed = passes_completed
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards

    @staticmethod
    def db_format(value_ls: list):
        return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_DB_FORMAT, value_ls)

    @staticmethod
    def db_edit_format(value_ls: list):
        return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_UPDATE_FORMAT, value_ls)

    @staticmethod
    def create_add_query(info_dict: dict):
        pass

    @staticmethod
    def search_by_atr(frontend_dict: dict):        
        return SoccerPlayerStatistic.get_by_attribute(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, frontend_dict, SoccerPlayerStatistic.CLASS_NAME, SoccerPlayerStatistic.ENTITY_TO_DB_MAPPING)

 