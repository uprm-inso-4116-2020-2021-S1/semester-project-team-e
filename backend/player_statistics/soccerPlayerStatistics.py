
from datetime import date
from player_statistics.playerStatistics import PlayerStatistic
from db_entity import DB_Entity

class SoccerPlayerStatistic():
    #
    # DATABASE_TABLE_NAME = 'soccer_individual_statistics'
    #
    # CLASS_NAME = 'SoccerPlayerStatistic'
    #
    # ENTITY_TO_DB_MAPPING = {
    #     CLASS_NAME : 'soccer_individual_statistics',
    #     'date' : 'year',
    # }
    #
    #
    # SOCCER_PLAYER_STATISTIC_FORMAT = DB_Entity._get_column_names(DATABASE_TABLE_NAME)
    #
    #
    #
    def __init__(self, statid, player_id, halve_number, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year):
        self.statid = statid
        self.player_id = player_id
        self.halve_number = halve_number
        self.goals_scored = goals_scored
        self.assists = assists
        self.tackles_won = tackles_won
        self.saves = saves
        self.passes_completed = passes_completed
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards
        self.year = year

    # def to_dictionary(self):
    #     ret_dict = {}
    #     for key, item in vars(self).items():
    #         if isinstance(item, date):
    #             # print(key)
    #             # print(item)
    #             self.date: date
    #             ret_dict[key] = self.date.strftime(r'%Y-%m-%d')
    #         else:
    #             ret_dict[key] = item
    #     return ret_dict
    #
    # @staticmethod
    # def db_format(value_ls: list):
    #     return dict(zip(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, value_ls))
    #     # return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, value_ls)
    #
    # # @staticmethod
    # # def db_edit_format(value_ls: list):
    # #     raise NotImplementedError
    # # #     key_ls = SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT
    # # #     # Assuming soccer player statistic id is given we can re append it last
    # # #     key_ls.append(key_ls[0])
    # # #     return SoccerPlayerStatistic._create_dict_format(SoccerPlayerStatistic.SOCCER_PLAYER_UPDATE_FORMAT, value_ls)
    #
    # @staticmethod
    # def create_add_query(info_dict: dict):
    #     pass
    #
    # @staticmethod
    # def search_by_atr(frontend_dict: dict):
    #     return SoccerPlayerStatistic.get_by_attribute(SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT, frontend_dict, SoccerPlayerStatistic.CLASS_NAME, SoccerPlayerStatistic.ENTITY_TO_DB_MAPPING)
    #
    # @staticmethod
    # def build_stat(value_ls):
    #     key_args = list(SoccerPlayerStatistic._get_column_names(SoccerPlayerStatistic.DATABASE_TABLE_NAME))
    #     dict_data = dict((zip(key_args, list(value_ls))))
    #     SoccerPlayerStatistic._fix_instance_names_to_db({'year':'date'}, dict_data)
    #     return SoccerPlayerStatistic(**dict_data) , dict_data
