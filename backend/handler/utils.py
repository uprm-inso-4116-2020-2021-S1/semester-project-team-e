from typing import List, Dict


''' Status Codes '''
OK = 200
CREATED = 201
ACCEPTED = 202
NOT_FOUND = 404
BAD_REQUEST = 400


DATABASECONFIG = {
    'host':'localhost',
    'user':'hector',
    'password':'pollo',
    'database':'project_db'
    }

def to_specified_format(info_list: List, des_format: List):
    ret_list = []
    for entry_tuple in info_list:
        ret_list.append(dict(zip(des_format, entry_tuple)))
    return ret_list

def connectDB():
    try:
        conn = mariadb.connect(**DATABASECONFIG)
    # except:
    #     conn = mariadb.connect(**DEFAULTDATABASECONFIG)
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


def generic_attribute_find(class_attributes: List, arguments: Dict, class_name: str):
    if len(arguments) < 1:
        print('No attributes provided, returning None')
        return None
    
    argument_ls = []
    for entry in arguments.keys():
        if entry in class_attributes:
            argument_ls.append(entry)

    mk_select_query = 'select '
    for item in argument_ls:
        mk_select_query += f'{item} '
    mk_select_query.join(f'from {class_name} where (')
    for item in argument_ls:
        current_item = argument_ls[item]
        if isinstance(current_item, str):
            mk_select_query += f'{item} = \'{arguments[item]}\''
        else:
            mk_select_query += f'{item} = {arguments[item]}'
        if item != argument_ls[-1]:
            mk_select_query += f' and '

    mk_select_query += ');'
    print(f'Constructed query is: {mk_select_query}')
    return mk_select_query
    

