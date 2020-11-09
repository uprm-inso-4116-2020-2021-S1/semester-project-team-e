from typing import List, Dict, Tuple, Union, Any
import re
import mariadb
from player.player import Player
# from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic


''' Status Codes '''
OK = 200
CREATED = 201
ACCEPTED = 202
NOT_FOUND = 404
BAD_REQUEST = 400



PLAYER_FORMAT = [
    'player_id',
    'player_name',
    'height',
    'weight',
    'team_name',
    'sport_name',
    'team_sport_id',
    'player_sport_stats'
]

PLAYER_DB_FORMAT = [        
    'player_id',
    'player_name',
    'height',
    'weight',
    'team_name',
    'sport_name',
    'team_sport_id',    
]

SOCCER_STATS_FORMAT = [
    'player_id',
    'position',
    'date',
    'halve_number',
    'games_played',
    'saves',
    'goals_scored',
    'assists',
    'tackles_won',
    'passes_completed',
    'red_cards',
    'yellow_cards'
]



DATABASECONFIG = {
    'host':'localhost',
    'user':'inso4116',
    'password':'letmein',
    'database':'sports_tracker'
    }

def to_specified_format(info_list: List, des_format: List):
    ret_list = []
    for entry_tuple in info_list:
        ret_list.append(dict(zip(des_format, entry_tuple)))
    return ret_list

def connectDB() -> mariadb._mariadb.connection:
    try:
        conn: mariadb._mariadb.connection
        conn = mariadb.connect(**DATABASECONFIG)        
    
    except Exception as e:
        print(f'Connection to the database failed with error:\n{e}')
    return conn


def checkDictEqualKeys(default_dict: Dict, target_dict: Dict):
    ''' Checks that both dictionaries contain the same keys and both are of the same lenght'''
    if len(default_dict) != len(target_dict):
        return False
    for entry in default_dict.keys():
        if entry not in target_dict.keys():
            return False
    return True

def extract_attribs(atr_dict: Dict, args: List):
    extract = []
    for entry in args:
        extract.append(atr_dict.get(entry, None)) 
    return extract


def connect_and_cursor() -> Tuple[mariadb._mariadb.connection, mariadb._mariadb.connection.cursor]:
    connection = connectDB()
    return connection, connection.cursor()


class AttributeFinder:

    # Esto esta basado en que la clase tenga el id de forma 'watever_id' sino no funcionará

    SELECT = 'select '
    ID_ATTRIBUTE = re.compile(r'[a-zA-Z]+_id')
    DEFAULT_CLASSES = [type(float), type(str), type(dict), type(list), type(int), type(tuple), type(bool), type(None)]
    DB_NAME_ASSOCIATION = {'Player' : 'player', 'SoccerPlayerStatistic' : 'soccer_individual_statistics'}
    DB_FORMAT_ASSOCIATION = {'Player' : PLAYER_DB_FORMAT}
    
    

    @staticmethod
    def generic_attribute_find_query(entity: type, argument_dict: Dict, debug: bool=False ) -> str:        
        atr = AttributeFinder        
        class_name = atr._get_class_name(entity)
        class_attributes = atr._get_class_attrbs(entity)
        current_entity_keys = atr._maintain_db_format(class_name, list(class_attributes.keys()))
        atr._check_id_entity_arg(argument_dict)
        valid_atr_dict = {}        
        if debug:
            print(class_name)
            print(class_attributes)            
            print(argument_dict)       
        
        for arg_key, arg_val in argument_dict.items():
            if arg_key in current_entity_keys:
                valid_atr_dict[arg_key] = arg_val

        current_query = atr.SELECT + atr.query_helper(current_entity_keys)
        if debug:
            print(current_query)
        current_query += f'from {atr.DB_NAME_ASSOCIATION.get(class_name, class_name) } where ' + atr._unpack_dict_db_format_comparison(argument_dict)        

        if debug:
            print(current_query)

        return current_query

    @staticmethod
    def _unpack_dict_db_format_comparison(arg_dict: Dict) -> str:
        ret_str = ''
        for idx, item_pair in enumerate(arg_dict.items()):
            key, value = item_pair
            # print(value, type(value))
            if idx == 0:
                if isinstance(value, str):
                    ret_str += f'{key} like {value}'
                else:
                    ret_str += f'{key} = {value}'
            else:
                if isinstance(value, str):
                    ret_str += f' or {key} like {value}'
                else:
                    ret_str += f' or {key} = {value}'

        return ret_str


    @staticmethod
    def _get_class_name(class_entity: Any) -> str:
        return type(class_entity).__name__

    @staticmethod
    def _check_id_entity_arg(args_dict: Dict):
        # Verifica que la referencia no cambie
        for key, entry in args_dict.items():
            if AttributeFinder.ID_ATTRIBUTE.search(key):
                args_dict['id'] = args_dict.pop(key)
                break        
        
    @staticmethod
    def _get_class_attrbs(entity: Any):
        entity_dict = {}        
        for key, entry in vars(entity).items():
            # print(type(entry))
            if type(entry) in AttributeFinder.DEFAULT_CLASSES:
                
                if AttributeFinder.ID_ATTRIBUTE.search(key):
                    entity_dict['id'] = entry
                else:
                    entity_dict[key] = entry
            
        return entity_dict


    @staticmethod
    def _maintain_db_format(entity: str, args_ls: List) -> None:        
        if AttributeFinder.DB_FORMAT_ASSOCIATION.get(entity, None):
            for item in args_ls:
                if item not in AttributeFinder.DB_FORMAT_ASSOCIATION[entity]:
                    if item != 'id':
                        args_ls.remove(item)

        return args_ls



    @staticmethod
    def query_helper(arguments_ls: List) -> str:
        mk_str = ''
        if arguments_ls == []:
            return mk_str
        if len(arguments_ls) == 1:
            return str(arguments_ls[0])
        else:
            for arg in arguments_ls[:-1]:
                mk_str += str(arg) + ', '
            mk_str += str(arguments_ls[-1]) + ' '
        return mk_str




class DAO:

    DATABASECONFIG = {
    'host':'localhost',
    'user':'inso4116',
    'password':'letmein',
    'database':'sports_tracker'
    }

    def __init__(self):
        self.current_connection: mariadb._mariadb.connection
        self.current_connection = mariadb.connect(**DAO.DATABASECONFIG)
        self.current_connection.autocommit = True
        self.cursor = self.current_connection.cursor()
        self.result = None

    def close_and_return_result(self):
        self.current_connection.close()
        return self.result

    def execute_query(self, query: str, args: List) -> None:
        if args:
            self.cursor.execute(query, tuple(args))    
        else:
            self.cursor.execute(query)
        
    def execute_query_and_fetch(self, query: str, args: List=None):
        if args:
            self.cursor.execute(query, tuple(args))    
        else:
            self.cursor.execute(query)
        try:
            self.result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return self.result


        
   
        
    

    
        



