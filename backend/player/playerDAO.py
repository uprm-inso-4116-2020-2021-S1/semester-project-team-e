import mariadb


# from typing import Dict
# from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
# from handler.utils import connectDB, connect_and_cursor, DAO, extract_attribs
# from dao.dummy_data import soccer_dummy_data
from player.player import Player
from handler import utils



class PlayerDAO:
    def __init__(self):
        self.conn = utils.connectDB()

    def getAll(self):
        cursor = self.conn.cursor()
        query = "SELECT player.id, playername, team_name, position, height, weight, sport_name from player ORDER BY team_sport_id"
        cursor.execute(query)
        result = cursor.fetchall()
        player_tup = [player for player in result]
        player_obj = [Player(player[0], player[1], player[2], player[3], player[4], player[5], player[6]) for player in player_tup]
        # for player in player_obj:
        #     SoccerPlayerStatisticDAO().getByPlayerid(player.player_id)
        cursor.close()
        self.conn.close()
        return player_obj

    def get(self, player_id):
        cursor = self.conn.cursor()
        query = "SELECT id, playername, team_name, position, height, weight, sport_name from player WHERE id = ?"
        cursor.execute(query, (player_id,))
        result = cursor.fetchall()
        cursor.close()
        return [Player(player[0], player[1], player[2], player[3], player[4], player[5], player[6]) for player in result]

    def getByTeamID(self, team_id):
        cursor = self.conn.cursor()
        query = "SELECT player.id, playername, player.team_name, position,  height, weight, sport_name FROM player JOIN team ON player.team_name = team.team_name WHERE team.id = ?"
        cursor.execute(query, (team_id,))
        result = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return [Player(player[0], player[1], player[2], player[3], player[4], player[5], player[6]) for player in result]
        

    # @classmethod
    # def get_by_attribute(cls, self, player_args: dict):
    #     select_query = Player.search_by_atr(player_args)
    #     self.execute_query_and_fetch(select_query)
    #     return self.close_and_return_result()
        

    def add(self, player):
        cursor = self.conn.cursor()
        query = "SELECT team_sport.id FROM ((team JOIN team_sport ON team.id = team_id) JOIN sport ON sport_id = sport.id) WHERE sportname = ? AND team_name = ?"
        cursor.execute(query, (player.sport_name, player.team_name,))
        sportid = cursor.fetchone()
        query2 = "INSERT INTO player (team_name, playername, position, height, weight, sport_name, team_sport_id) values(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query2, (player.team_name, player.player_name, player.position, player.height, player.weight, player.sport_name, sportid,))
        playerid = cursor.lastrowid
        player_obj = self.get(playerid)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return player_obj
        

    # def edit(self, player_info: Dict):
    #     edit_query = 'update player set player_name = ?, height = ?, weight = ?, team_name = ?, sport_name = ? where id = ?'
    #     self.cursor.execute(edit_query, (extract_attribs(player_info, Player.PLAYER_UPDATE_FORMAT)))
    #     self.close_and_return_result()
    #     return self.result
    #
    #
    # def delete(self, player_id: int):
    #     delete_query = 'delete from player where id = ?'
    #     self.cursor.execute(delete_query, (player_id,))
    #     return self.close_and_return_result()
        
        



