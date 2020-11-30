import mariadb


from typing import Dict
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from handler.utils import connectDB, connect_and_cursor, DAO, extract_attribs
from dao.dummy_data import soccer_dummy_data
from player.player import Player


class PlayerDAO(DAO):  
    

    def get_all(self):                
        query = 'select * from player'                
        self.execute_query_and_fetch(query)        
        return self.result

    def get(self, player_id):        
        select_query = Player.search_by_atr({'id' : player_id})
        self.execute_query_and_fetch(select_query)
        return self.close_and_return_result()        
        

    
    def get_by_attribute(self, player_args: dict):        
        select_query = Player.search_by_atr(player_args)
        self.execute_query_and_fetch(select_query)
        return self.close_and_return_result()        
        

    def add(self, player_info: dict):        
        add_query = 'insert into player (player_name, height, weight, team_name, sport_name) values(%(player_name)s, %(height)s, %(weight)s, %(team_name)s, %(sport_name)s)'
        self.execute_query_and_fetch(add_query, player_info)        
        self.close_and_return_result()
        if self.cursor.lastrowid:
            last_player_id = self.cursor.lastrowid            
            return last_player_id
        else:
            return None
        

    def edit(self, player_info: Dict):
        self._disable_foreign_key()
        edit_query = 'update player set player_name = ?, height = ?, weight = ?, team_name = ?, sport_name = ?, team_sport_id = ? where id = ?'
        self.cursor.execute(edit_query, (extract_attribs(player_info, Player.PLAYER_UPDATE_FORMAT)))        
        self._enable_foreign_key()
        self.close_and_return_result()        
        return self.result      


    def delete(self, player_id: int):
        delete_query = 'delete from player where id = ?'
        self.cursor.execute(delete_query, (player_id,))
        return self.close_and_return_result()

    def getAllPlayerId(self) -> None:
        select_query = 'select id from player'
        self.execute_query_and_fetch(select_query)
        return self.close_and_return_result()
        
        



