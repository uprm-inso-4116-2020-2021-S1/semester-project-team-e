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
        player_cont = []
        for idx, player in enumerate(player_list):            
            player = self.get(player['player_id'])            
            if player:
                player_cont.append(vars(player))
        return player_cont       

    def get(self, player_id):
        player_id = int(player_id)     
        player = PlayerDAO().get(player_id)        
        if player:
            player_socc_stat = SoccerPlayerStatisticDAO().get_by_attribute({'player_id' : player_id})
            if player_socc_stat:
                for idx, stat in enumerate(player_socc_stat):                    
                    _, player_socc_stat[idx] = SoccerPlayerStatistic.build_stat(stat)                
            current_player = Player(**(to_specified_format(player, PLAYER_FORMAT)[0]))
            current_player.player_sport_stats =  {'SoccerPlayerStatistics' : player_socc_stat}
            return current_player            
        else:
            return None    

    def add(self, player: Player):
        player_json = player.to_db_format()
        return PlayerDAO().add(player_json)

    def edit(self, player_info):
        player_info = player_info.to_specified_db_format(Player.PLAYER_UPDATE_FORMAT)
        return PlayerDAO().edit(player_info)
        

    def delete(self, player_id):
        return PlayerDAO().delete(player_id)
        
    
    def getPlayerByAttributes(self, attributes):
        query = AttributeFinder.generic_attribute_find_query(SoccerPlayerStatistic(), attributes)
        # print(f'Query in get player by attribute is: {query}')
        player = PlayerDAO().get_by_attribute(attributes)
        # print(player)
        # TODO Termina esto
        return player

    def getAllPlayerStatistics(self):
        player_stats = SoccerPlayerStatisticDAO().getAll()
        player_stats = to_specified_format(player_stats, SoccerPlayerStatistic.SOCCER_PLAYER_STATISTIC_FORMAT)
        for idx, stat in enumerate(player_stats):
            player_stats[idx], _ = SoccerPlayerStatistic.build_stat(stat.values())
        return player_stats


