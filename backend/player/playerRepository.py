from flask import jsonify
from player.player import Player
from player_statistics.playerDAO import SoccerPlayerStatisticDAO, PlayerDAO
from handler.utils import to_specified_format
from dao.dummy_data import player_dat

PLAYER_FORMAT = [
    'player_id',
    'player_name',
    'height',
    'weight',
    'team_name',
    'sport_name',
    'team_sport_id',
    'player_sport_stats'
]

SOCCER_STATS_FORMAT = [
    'player_id',
    'position',
    'date',
    'halve_number',
    'games_played',
    'saves',
    'goals_scored',
    'assists',
    'tackles_won',
    'passes_completed',
    'red_cards',
    'yellow_cards'
]

class PlayerRepository:
    
    def getAll(self):
        player_list = PlayerDAO().get_all()
        player_sports_stats = SoccerPlayerStatisticDAO().getAll()
        for idx, player in player_list:
            player_info = to_specified_format(player, PLAYER_FORMAT[:-1])
            player_stat_info = None
            for stat in player_sports_stats:
                stat = to_specified_format(stat, SOCCER_STATS_FORMAT)
                if stat['player_id'] == player_info['player_id']:
                    player_stat_info = stat
                    break
            player_info['player_sport_stats'] = player_stat_info
            player_list[idx] = Player(**player_info)
        return player_list
        # return [Player(**player_info) for player_info in player_dat]
        

    def get(self, player_id):     
        player = PlayerDAO().get(player_id)
        if player:
            player = to_specified_format(player, PLAYER_FORMAT[:-1])
            stat = SoccerPlayerStatisticDAO().get(player_id)
            player['player_sport_stats'] = stat
        return Player(**player)
        # player = [player for player in player_dat if player['player_id'] == player_id]
        # if player:
        #     return Player(**player[0])
        # else:
        #     return None

    def add(self, player_info):
        return Player(**player_dat[2])

    def edit(self, player_info):
        return Player(**player_dat[1])

    def delete(self, player_id):
        return Player(**player_dat[0])

    def getBySportName(self, sport_name):
        return Player(**player_dat[1])

    def getByName(self, player_name):
        return Player(**player_dat[2])

    def getByTeamName(self, team_name):
        return Player(**player_dat)[1]

    def getByHeight(self, height):
        return Player(**player_dat[0])

    def getByWeight(self, weight):
        return Player(**player_dat[2])

    def getPlayerByAttributes(self, attributes):
        return Player(**player_dat[1])