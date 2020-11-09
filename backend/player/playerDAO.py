import mariadb


from typing import Dict
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from handler.utils import connectDB, connect_and_cursor, PLAYER_FORMAT, DAO, AttributeFinder, extract_attribs
from dao.dummy_data import soccer_dummy_data
from player.player import Player




class PlayerDAO(DAO):
    
    _DUMMY_PLAYER = Player()
    _DUMMY_INDIVIDUAL_SOCCER_STAT = SoccerPlayerStatistic()

    def get_all(self):                
        query = 'select * from player'                
        self.execute_query_and_fetch(query)        
        return self.result

    def get(self, player_id):
        query = AttributeFinder.generic_attribute_find_query(PlayerDAO._DUMMY_PLAYER, {'player_id' : player_id})
        print(query)        
        return self.execute_query_and_fetch(query)

    def add(self, player_info: Dict):
        print(player_info)
        add_query = 'insert into player (player_name, height, weight, team_name, sport_name) values(?, ?, ?, ?, ?)'
        print(add_query)
        print(extract_attribs(player_info, Player.PLAYER_DB_ADD_FORMAT))
        self.cursor.execute(add_query, extract_attribs(player_info, Player.PLAYER_DB_ADD_FORMAT))        
        self.close_and_return_result()
        if self.cursor.lastrowid:
            last_player_id = self.cursor.lastrowid
            print(last_player_id)
            return last_player_id
        else:
            return None

    def edit(self, player_info: Dict):        
        # Si team sport id no existe da un error
        #Algunos args estan causando errores.
        edit_query = 'update player set player_name = ?, height = ?, weight = ?, team_name = ?, sport_name = ? where id = ?'
        self.cursor.execute(edit_query, (extract_attribs(player_info, Player.PLAYER_UPDATE_FORMAT)))        
        self.close_and_return_result()        
        return self.result


    def delete(self, player_id: Dict):
        delete_query = 'delete from player where id = ?'
        self.cursor.execute(delete_query, (player_id,))
        return self.close_and_return_result()
        



