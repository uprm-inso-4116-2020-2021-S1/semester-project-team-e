from typing import Dict
from handler.utils import DAO
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic





class SoccerPlayerStatisticDAO(DAO):

    
    def getAll(self):
        query = 'select * from soccer_individual_statistics'
        self.execute_query_and_fetch(query)
        self.close_and_return_result()
        return self.result

    def get(self, stat_id):
        get_query = 'select * from soccer_individual_statistics where id = ?'
        self.execute_query_and_fetch(get_query, [stat_id])
        return self.close_and_return_result()


    def add(self, stat: Dict):
        add_query = 'insert into soccer_individual_statistics (player_id, games_played, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        stat_info = SoccerPlayerStatistic.db_format(stat.values())
        self.execute_query_and_fetch(add_query, stat_info)
        # self.cursor.execute(add_query, stat_info)
        self.close_and_return_result()
        if self.cursor.lastrowid:
            last_stat_id = self.cursor.lastrowid
            print(last_stat_id)
            return last_stat_id
        else:
            return None

    def edit(self, stat:Dict):
        edit_query = '''
        update soccer_individual_statistics set 
        player_id = ?, games_played = ?, goals_scored = ?, assists = ?,
        tackles_won = ?, saves = ?, passes_completed = ?, yellow_cards = ?,
        red_cards = ?, year = ?
        where id = ?
        '''
        self.execute_query_and_fetch(edit_query, SoccerPlayerStatistic.db_edit_format(stat.values()))
        # self.cursor.execute(edit_query, SoccerPlayerStatistic.db_edit_format(stat.values()))
        self.close_and_return_result()
        return self.result

    def delete(self, stat_id):
        delete_query = 'delete from player where id = ?'
        self.execute_query_and_fetch(delete_query, [stat_id])
        # self.cursor.execute(delete_query, stat_id)
        return self.close_and_return_result()

    def get_by_attribute(self, json_recv_data):
        select_query = SoccerPlayerStatistic.search_by_atr(json_recv_data)
        print(select_query)
        self.execute_query_and_fetch(select_query)
        print('result!!!!! ->  ', self.result)
        return self.close_and_return_result()
        
        
        
