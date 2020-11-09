from flask import jsonify
from player.player import Player
from player.playerDAO import PlayerDAO
from player_statistics.soccerPlayerStatisticDAO import SoccerPlayerStatisticDAO
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from handler.utils import to_specified_format
from dao.dummy_data import player_dat
from handler.utils import PLAYER_FORMAT, SOCCER_STATS_FORMAT, PLAYER_DB_FORMAT, AttributeFinder


class PlayerRepository:
    
    def getAll(self):
        player_list = PlayerDAO().get_all()
        player_list = to_specified_format(player_list, PLAYER_FORMAT[:-1])
        # print(player_list)
        player_sports_stats = SoccerPlayerStatisticDAO().getAll()
        for idx, player in enumerate(player_list):            
            player_info = player
            player_stat_info = None

            # TODO Implement the part with the player stats
            player_list[idx] = Player(**player_info)
        return player_list       

    def get(self, player_id):
        player_id = int(player_id)     
        player = PlayerDAO().get(player_id)
        print(player)
        if player:
            player_socc_stat = SoccerPlayerStatisticDAO().get_by_attribute({'player_id' : player_id})
            if player_socc_stat:
                print(player_socc_stat)

            return Player(**(to_specified_format(player, PLAYER_FORMAT)[0]))
            
        else:
            return None    

    def add(self, player: Player):
        player_json = player.to_db_format()
        return PlayerDAO().add(player_json)

    def edit(self, player_info):
        player_info = player_info.to_specified_db_format(Player.PLAYER_UPDATE_FORMAT)
        return PlayerDAO().edit(player_info)
        # return Player(**player_dat[1])

    def delete(self, player_id):
        return PlayerDAO().delete(player_id)
        # return Player(**player_dat[0])
    
    def getPlayerByAttributes(self, attributes):
        query = AttributeFinder.generic_attribute_find_query(SoccerPlayerStatistic._DUMMY_SOCCER_STAT, attributes)
        print(f'Query in get player by attribute is: {query}')
        player = PlayerDAO().get(attributes)
        # if player:
        # TODO Termina esto
        return None

    def getAllPlayerStatistics(self):
        return None

    def getPlayerStatById(self, stat_id):
            return None    

    def addPlayerStat(self, player_stat ):
        return None

    def editPlayerStat(self, player_stat):
        return None

    def deletePlayerStat(self, player_stat_id):
        return None
    
    def getPlayerStatByAttributes(self, attributes):
        return None