from flask import jsonify
from player.player import Player
from player.playerDAO import PlayerDAO
from handler.utils import to_specified_format, DAO
from player_statistics.soccerPlayerStatisticDAO import SoccerPlayerStatisticDAO
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic

from dao.dummy_data import player_dat


TABLE_NAME_INDEX = 0
DAO_TYPE = 1
ENTITY_TYPE =2
# Por cada tipo de individual player statistic se añade el nombre de la tabla en la base de datos
INDIVIDUAL_DB_STATISTICS = {
    'soccer' : ('soccer_individual_statistics', SoccerPlayerStatisticDAO, 'SoccerPlayerStatistic'),    
}



class PlayerRepository:
    
    def getAllPlayer(self):
        ''' Only gets all Players ''' 
        p_dao = PlayerDAO()
        player_keys = Player.PLAYER_DB_FORMAT
        player_list = p_dao.get_all()        
        player_list = to_specified_format(player_list, player_keys)        
        player_cont = []
        for idx, player in enumerate(player_list):                        
            player = self.getPlayerByID(player['id'])            
            if player:
                player_cont.append(vars(player))
        return player_cont       

    def getPlayerByID(self, player_id):
        ''' Get player by id only ''' 
        player_id = int(player_id)     
        player = PlayerDAO().get(player_id)        
        if player:
            current_player = to_specified_format(player, Player.PLAYER_DB_FORMAT)
            return current_player            
        else:
            return None    

    def getPlayerAndStats(self, player_id):
        ''' Only gets player by id and any sport statistics related with the player id ''' 
        player_id = int(player_id)     
        player = self.getPlayerByID(player_id)
        player_stats = []
        if player:
            player = player[0]
            player_stats = self.getPlayerStatisticsByPlayerId(player_id)            
            player['PlayerStatistics'] = player_stats
            return player            
        else:
            return None    

    def addPlayer(self, player: dict):        
        return PlayerDAO().add(player)

    def editPlayer(self, player_info):
        ''' Replaces given player with the player specified '''
        if player_info.get('id', None):
            player_info['player_id'] = player_info['id']
            player_info.pop('id')
        player_info = Player(**player_info)
        player_info: Player        
        player_info = player_info.to_specified_db_format(Player.PLAYER_UPDATE_FORMAT)
        p_dao = PlayerDAO()
        player_result = PlayerDAO().edit(player_info)
        if player_result:
            return player_result
        else:
            return None
        

    def deletePlayer(self, player_id):        
        return PlayerDAO().delete(player_id)
        
    
    def getPlayerByAttributes(self, attributes: dict) -> list:
        ''' Only returns list players that contain all the given attributes given in the search '''         
        
        players = PlayerDAO().get_by_attribute(attributes)
        if players:
            players = to_specified_format(players, Player.PLAYER_DB_FORMAT)
            return players
        else:
            return None
        

    def getAllPlayerStatistics(self):
        ''' Gets every individual player statistic regardless of player or sport ''' 
        stat_ls = []
        for stat_type in INDIVIDUAL_DB_STATISTICS.values():
            stat_dao = stat_type[DAO_TYPE]
            stat_type = stat_type[TABLE_NAME_INDEX]
            receive_ls = self._genericGetAllTable(stat_dao)
            if receive_ls:
                entity_keys = DAO()._get_column_names(stat_type)
                receive_ls = to_specified_format(receive_ls, entity_keys)
                stat_ls.extend(receive_ls)
        return stat_ls


    def getPlayerStatById(self, sport_type: str, stat_id: int):
        dao_type = INDIVIDUAL_DB_STATISTICS.get(sport_type, None)
        if dao_type:
            dao_type = dao_type[DAO_TYPE]
            return self._genericGetByIdTable(dao_type, stat_id)
        else:
            return None

    def getPlayerStatisticsByPlayerId(self, player_id):
        ''' Gets stats by player id '''
        stat_ls = []
        for sport, stat_type in INDIVIDUAL_DB_STATISTICS.items():
            stat_name = stat_type[TABLE_NAME_INDEX]
            stat_type = stat_type[DAO_TYPE]            
            receive_ls = self._genericGetByPlayerIdTable(stat_type, player_id)
            if receive_ls:
                entity_keys = DAO()._get_column_names(stat_name)
                receive_ls = to_specified_format(receive_ls, entity_keys)                
                stat_dict = {INDIVIDUAL_DB_STATISTICS[sport][ENTITY_TYPE] : receive_ls}
                stat_ls.append(stat_dict)
        return stat_ls

    def _genericGetAllTable(self, entity_dao: DAO) -> list:        
        info_ls = entity_dao().getAll()        
        if isinstance(info_ls, list) or isinstance(info_ls, tuple) or isinstance(info_ls, iter):
            return info_ls
        else:
            raise TypeError(f'Returned object of type {type(info_ls)}')

    def _genericGetByIdTable(self, entity_dao: DAO, player_id: int) -> list:
        entity_dao: DAO
        info_ls = entity_dao().get(player_id)        
        print(info_ls)
        if info_ls and (isinstance(info_ls, list) or isinstance(info_ls, tuple) or isinstance(info_ls, iter)):
            return info_ls
        else:
            return []

    # def getStatByPId(self, player_id):
    #     stat_ls = []
    #     for sport, stat_type in INDIVIDUAL_DB_STATISTICS.items():
    #         stat_name = stat_type[TABLE_NAME_INDEX]
    #         stat_type = stat_type[DAO_TYPE]            
    #         receive_ls = self._genericGetByPlayerIdTable(stat_type, player_id)
    #         if receive_ls:
    #             entity_keys = DAO()._get_column_names(stat_name)
    #             receive_ls = to_specified_format(receive_ls, entity_keys)                
    #             stat_dict = {INDIVIDUAL_DB_STATISTICS[sport][ENTITY_TYPE] : receive_ls}
    #             stat_ls.append(stat_dict)
    #     return stat_ls

   

    def _genericGetByPlayerIdTable(self, entity_dao: DAO, player_id: int) -> list:
        entity_dao: DAO
        info_ls = entity_dao().get_by_attribute({'player_id': player_id})
        print(info_ls)
        if info_ls and (isinstance(info_ls, list) or isinstance(info_ls, tuple) or isinstance(info_ls, iter)):
            return info_ls
        else:
            return []

    def _getAllPlayerIds(self) -> list:
        id_result = PlayerDAO().getAllPlayerId()
        if id_result:
            for idx, itm in enumerate(id_result):
                id_result[idx] = itm[0]
            return id_result
        else:
            return []

    
