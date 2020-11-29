from typing import Dict
from backend.handler import utils
from backend.player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic


class SoccerPlayerStatisticDAO():
    def __init__(self):
        self.conn = utils.connectDB()
    
    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT id, player_id, half, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year FROM soccer_individual_statistics ORDER BY player_id"
        cursor.execute(query)
        result = cursor.fetchall()
        stat_tup = [stat for stat in result]
        stat_obj = [SoccerPlayerStatistic(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8], stat[9], stat[10]) for stat in stat_tup]
        cursor.close()
        self.conn.close()
        return stat_obj

    def get(self, stat_id):
        cursor = self.conn.cursor()
        query = "SELECT id, player_id, half, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year FROM soccer_individual_statistics WHERE id = ?"
        cursor.execute(query, (stat_id,))
        result = cursor.fetchall()
        cursor.close()
        return [SoccerPlayerStatistic(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8], stat[9], stat[10]) for stat in result]

    def getByTeamID(self, team_id):
        cursor = self.conn.cursor()
        query = "SELECT soccer_individual_statistics.id, player_id, half, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year FROM (soccer_individual_statistics JOIN player ON player_id = player.id) JOIN team ON player.team_name = team.team_name WHERE team.id = ?"
        cursor.execute(query, (team_id,))
        result = cursor.fetchall()
        stat_tup = [stat for stat in result]
        stat_obj = [SoccerPlayerStatistic(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8], stat[9], stat[10]) for stat in stat_tup]
        cursor.close()
        return stat_obj


    def add(self, soccerPlayerStatistic):
        cursor = self.conn.cursor()
        query = "INSERT INTO soccer_individual_statistics(player_id, half, goals_scored, assists, tackles_won, saves, passes_completed, yellow_cards, red_cards, year) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (soccerPlayerStatistic.player_id, soccerPlayerStatistic.halve_number, soccerPlayerStatistic.goals_scored, soccerPlayerStatistic.assists, soccerPlayerStatistic.tackles_won, soccerPlayerStatistic.saves, soccerPlayerStatistic.passes_completed, soccerPlayerStatistic.yellow_cards, soccerPlayerStatistic.red_cards, soccerPlayerStatistic.year,))
        statid = cursor.lastrowid
        stat_obj = self.get(statid)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return stat_obj

    def edit(self, stat:dict):
        edit_query = '''
        update soccer_individual_statistics set 
        id = ?, player_id = ?, games_played = ?, goals_scored = ?, assists = ?,
        tackles_won = ?, saves = ?, passes_completed = ?, yellow_cards = ?,
        red_cards = ?, year = ?
        where id = ?
        '''
        value_list = list(stat.values())
        value_list.append(value_list[0]) # Assumiendo que nos pasan el id del player stat, lo añadimos al final 
        self.execute_query_and_fetch(edit_query, value_list)        
        self.close_and_return_result()        
        return self.get_valid_result()

    def delete(self, stat_id):
        delete_query = 'delete from soccer_individual_statistics where id = ?'
        self.execute_query_and_fetch(delete_query, (stat_id, ))        
        return self.close_and_return_result()

    def get_by_attribute(self, json_recv_data):
        select_query = SoccerPlayerStatistic.search_by_atr(json_recv_data)        
        self.execute_query_and_fetch(select_query)        
        return self.close_and_return_result()
        
        
        
