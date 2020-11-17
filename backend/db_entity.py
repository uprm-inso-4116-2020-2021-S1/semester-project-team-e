import mariadb




class DB_Entity:


    @staticmethod
    def _get_column_names(target_table: str):
        col_query = 'select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME=\'' + target_table + '\''
        conn = mariadb.connect(**{'host':'localhost','user':'inso4116', 'password':'letmein', 'database':'sports_tracker'})
        c_cursor = conn.cursor()        
        c_cursor.execute(col_query)        
        result = c_cursor.fetchall()             
        conn.close()        
        pret_ls = []        
        for entry in result:
            for val in entry:
                if val:
                    pret_ls.append(val)
        return pret_ls


    @staticmethod
    def _create_dict_format(key_ls: list, val_ls: list):
        ''' zip function: "am i joke to you"'''
        ret_dict = {}
        if len(key_ls) != len(val_ls):            
            print('Bad list length.')
            raise ValueError(len(key_ls), ' vs ', len(val_ls))
        for idx, entry in enumerate(key_ls):
            ret_dict[entry] = val_ls[idx] 
        return ret_dict

    @staticmethod
    # TODO esto no creo que se esta usando atm
    def _find_attribute(attribute_key: str, entity_atr_list: list):
        if attribute_key in entity_atr_list:
            return True
        return False


    @staticmethod
    def _unpack_dict_db_format_comparison(arg_dict: dict) -> str:
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
    def _fix_instance_names_to_db(name_dict: dict, entity_dict: dict) -> None:        
        for db_name, db_val in name_dict.items():
            if entity_dict.get(db_name, None):
                entity_dict[db_val] = entity_dict[db_name]
                entity_dict.pop(db_name)

    @staticmethod
    def _query_helper(arguments_ls: list) -> str:
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

    @staticmethod
    def get_by_attribute(attribute_key_list: list, front_end_data_dict: dict, entity_name: str, database_name_mappings: dict):
        ''' primer arg es la lista en el orden que se quiere escribir el query para el search '''
        # valid_atr = []
        valid_front_end_dict: dict = {}
        atr_search_query = 'select ' # start creating query

        # populate a valid dictionary
        
        for atr in attribute_key_list:
            if atr in front_end_data_dict.keys():
                valid_front_end_dict[atr] = front_end_data_dict[atr]
        # dictionary should countain valid key entries, everything else should have been dropped
        # print(attribute_key_list)
        # print(database_name_mappings)
        for idx, entry in enumerate(attribute_key_list):
            # print(entry)
            if entry in database_name_mappings.keys():
                # print(entry)
                attribute_key_list[idx] = database_name_mappings[entry]
        # print(attribute_key_list)

        # fix attribute names first
        DB_Entity._fix_instance_names_to_db(database_name_mappings, front_end_data_dict)
        # check entity to instance name
        if entity_name in database_name_mappings.keys():
            entity_name = database_name_mappings[entity_name]  
        
        atr_search_query += DB_Entity._query_helper(attribute_key_list) + ' from ' + entity_name + ' where '# Tengo el select mas los atributos que quiero buscar
        atr_search_query += DB_Entity._unpack_dict_db_format_comparison(front_end_data_dict)

        return atr_search_query


