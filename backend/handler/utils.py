from typing import List, Dict, Tuple, Union, Any
import re
import mariadb
import sys
import json




''' Status Codes '''
OK = 200
CREATED = 201
ACCEPTED = 202
NOT_FOUND = 404
BAD_REQUEST = 400
CONFLICT = 409

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


class DAO(object):

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
        
        
        

    def _disable_foreign_key(self):        
        self.cursor.execute('SET SESSION foreign_key_checks=OFF;')
    
    def _enable_foreign_key(self):
        self.cursor.execute('SET SESSION foreign_key_checks=ON;')
        
        
        

    def close_and_return_result(self):
        ''' Closes connection and returns result obtained if valid, otherwise returns None'''
        self.current_connection.close()
        return self.get_valid_result()
        

    def execute_query(self, query: str, args: List) -> None:        
        if args:
            self.cursor.execute(query, tuple(args))    
        else:
            self.cursor.execute(query)
        
        
    def execute_query_and_fetch(self, query: str, args: List=None):
        if args:
            if isinstance(args, dict):
                self.cursor.execute(query, args)    
            else:
                self.cursor.execute(query, tuple(args))    
        else:
            self.cursor.execute(query)
        try:
            self.result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return self.result

    
    def _get_column_names(self, target_table: str):
        col_query = 'select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME=\'' + target_table + '\''
        self.execute_query_and_fetch(col_query)        
        self.close_and_return_result()
        pret_ls = []
        for entry in self.result:
            for val in entry:
                if val:
                    pret_ls.append(val)
        return pret_ls

    def get_valid_result(self):
        ''' Returns result of operation if any, otherwise returns None '''
        if self.result:
            return self.result
        else:
            return None
        

    @classmethod
    def getALL(cls, self):
        raise NotImplementedError

    @classmethod
    def get(cls, self, entity_id):
        raise NotImplementedError
    
    @classmethod
    def get_by_attribute(cls, self):
        raise NotImplementedError



def intoJSON(obj):
  return json.dumps(obj, default=lambda o: o.__dict__)


DATABASECONFIG = {
    'host' : 'localhost',
    'user' : 'inso4116',
    'password' : 'letmein',
    'database' : 'sports_tracker',
    'port' : 3306,
}

def connectDB():
    # global conn
    try:
        conn = mariadb.connect(**DATABASECONFIG
            # host= 'localhost',
            # user= 'inso4116',
            # password= 'letmein',
            # database= 'sports_tracker',
            # port = 3306
        )
    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    return conn


