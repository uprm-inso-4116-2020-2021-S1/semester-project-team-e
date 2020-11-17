
from datetime import date
from player_statistics.playerStatistics import PlayerStatistic
from db_entity import DB_Entity




# 'soccer_individual_statistics'

class SoccerPlayerStatistic(PlayerStatistic):

    DATABASE_TABLE_NAME = 'soccer_individual_statistics'

    CLASS_NAME = 'SoccerPlayerStatistic'

    ENTITY_TO_DB_MAPPING = {
        CLASS_NAME : 'soccer_individual_statistics',
        'date' : 'year',
    }

    
    SOCCER_PLAYER_STATISTIC_FORMAT = DB_Entity._get_column_names(DATABASE_TABLE_NAME)
    

    SOCCER_PLAYER_STATISTIC_DB_FORMAT = [
        # TODO ver que vas a hacer con el nombre de date y year que aparecen distintos en el codigo y en la base de datos
    ]

    SOCCER_PLAYER_UPDATE_FORMAT = [
        # TODO
    ]
    
    

    # TODO cambiar el db para que el stat sea determinado solo con el player id y removerle el id
    def __init__(self, id = None, player_id=None, position=None, date=None, halve_number=None, games_played=None, saves=None, goals_scored=None, assists=None, tackles_won=None, passes_completed=None, red_cards=None, yellow_cards=None):
        super(SoccerPlayerStatistic, self).__init__(player_id, position, date, games_played)                
        self.id = id
        self.halve_number = halve_number
        self.saves = saves
        self.goals_scored = goals_scored
        self.assists = assists
        self.tackles_won = tackles_won
        self.passes_completed = passes_completed
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards

    def to_dictionary(self):
        ret_dict = {}
        for key, item in vars(self).items():
            if isinstance(item, date):
                # print(key)
                # print(item)
                self.date: date 
                ret_dict[key] = self.date.strftime(r'%Y-%m-%d')
            else:
                ret_dict[key] = item
        return ret_dict

    @staticmethod
    def db_format(value_ls: list):
        return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, value_ls)

    @staticmethod
    def db_edit_format(value_ls: list):
        return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_UPDATE_FORMAT, value_ls)

    @staticmethod
    def create_add_query(info_dict: dict):
        pass

    @staticmethod
    def search_by_atr(frontend_dict: dict):        
        return SoccerPlayerStatistic.get_by_attribute(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, frontend_dict, SoccerPlayerStatistic.CLASS_NAME, SoccerPlayerStatistic.ENTITY_TO_DB_MAPPING)

    @staticmethod
    def build_stat(value_ls):        
        key_args = list(SoccerPlayerStatistic._get_column_names(SoccerPlayerStatistic.DATABASE_TABLE_NAME))        
        dict_data = dict((zip(key_args, list(value_ls))))        
        SoccerPlayerStatistic._fix_instance_names_to_db({'year':'date'}, dict_data)
        return SoccerPlayerStatistic(**dict_data) , dict_data
