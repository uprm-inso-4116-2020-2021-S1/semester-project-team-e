from typing import List
from typing import Dict
import json

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