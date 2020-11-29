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
    'soccer' : ('soccer_individual_statistics', 'SoccerPlayerStatisticDAO', 'SoccerPlayerStatistic'),
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
            player = self.get(player['id'])
            if player:
                player_cont.append(vars(player))
        return player_cont

    def getPlayerByID(self, player_id):
        ''' Get player by id only '''
        player_id = int(player_id)
        player = PlayerDAO().get(player_id)
        if player:
            current_player = dict(zip(player, Player.PLAYER_DB_FORMAT))
            return current_player
        else:
            return None

    def getPlayerAndStats(self, player_id):
        ''' Only gets player by id and any sport statistics related with the player id '''
        player_id = int(player_id)
        player = self.getPlayerByID(player_id)
        player_stats = []
        if player:
            player_stats = self.getPlayerStatisticsByPlayerId(player_id)
            current_player = to_specified_format(player, Player.PLAYER_DB_FORMAT)[0]
            current_player['PlayerStatistics'] = player_stats
            return current_player
        else:
            return None

    def addPlayer(self, player: Player):
        # Pending Revision
        player_json = player.to_db_format()
        return PlayerDAO().add(player_json)

    def editPlayer(self, player_info):
        # Pending Revision
        player_info = player_info.to_specified_db_format(Player.PLAYER_UPDATE_FORMAT)
        return PlayerDAO().edit(player_info)


    def deletePlayer(self, player_id):
        # Pending Revision
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
            stat_type = stat_type[TABLE_NAME_INDEX]
            receive_ls = self._genericGetAllTable(stat_type)
            if receive_ls:
                entity_keys = DAO._get_column_names(INDIVIDUAL_DB_STATISTICS[stat_type][TABLE_NAME_INDEX])
                receive_ls = to_specified_format(receive_ls, entity_keys)
                stat_ls.extend(receive_ls)

    def getPlayerStatisticsByPlayerId(self, player_id):
        stat_ls = []
        for stat_type in INDIVIDUAL_DB_STATISTICS.values():
            stat_type = stat_type[TABLE_NAME_INDEX]
            receive_ls = self._genericGetByIdTable(stat_type, player_id)
            if receive_ls:
                entity_keys = DAO._get_column_names(INDIVIDUAL_DB_STATISTICS[stat_type][TABLE_NAME_INDEX])
                receive_ls = to_specified_format(receive_ls, entity_keys)
                stat_ls.extend(receive_ls)

    def _genericGetAllTable(self, entity_dao: str) -> list:
        dao_function = f'{entity_dao}().getAll()'
        info_ls = eval(dao_function)
        if isinstance(info_ls, list) or isinstance(info_ls, tuple) or isinstance(info_ls, iter):
            return info_ls
        else:
            raise TypeError(f'Returned object of type {type(info_ls)}')

    def _genericGetByIdTable(self, entity_dao: str, player_id) -> list:
        dao_function = f'{entity_dao}().get({player_id})'
        info_ls = eval(dao_function)
        if isinstance(info_ls, list) or isinstance(info_ls, tuple) or isinstance(info_ls, iter):
            return info_ls
        else:
            raise TypeError(f'Returned object of type {type(info_ls)}')

    
