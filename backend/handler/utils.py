import sys
from typing import List
from typing import Dict
import json
import mariadb

''' Status Codes '''
OK = 200
CREATED = 201
ACCEPTED = 202
NOT_FOUND = 404
BAD_REQUEST = 400

def to_specified_format(info_list: List, des_format: List):
    ret_list = []
    for entry_tuple in info_list:
        ret_list.append(dict(zip(des_format, entry_tuple)))
    return ret_list

def intoJSON(obj):
  return json.dumps(obj, default=lambda o: o.__dict__)


DATABASECONFIG = {
    'host' : 'localhost',
    'user' : 'inso4116',
    'password' : 'letmein',
    'database' : 'sports_tracker',
}

def connectDB():
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