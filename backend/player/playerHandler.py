import json
from typing import List, Dict
from backend.player.player import Player
from backend.player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from backend.player.playerRepository import PlayerRepository
from backend.handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND

from flask import jsonify

from backend.player.playerDAO import PlayerDAO
from backend.player_statistics.soccerPlayerStatisticDAO import SoccerPlayerStatisticDAO


class PlayerHandler():
    
    def getAll(self):
        players = PlayerDAO().getAll()
        return jsonify(Players = [ player.serialize() for player in players ]), OK

    def add(self, json):
        if json['team_name'] and json['player_name'] and json['position'] and json['height'] and json['weight'] and json['sport_name']:
            new_player = Player(0, json['team_name'], json['player_name'], json['position'], json['height'], json['weight'], json['sport_name'])
            players = PlayerDAO().add(new_player)
            return jsonify(Players=[player.serialize() for player in players]), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def edit(self, json_obj: Dict, player_id: int):
        # Pending Revision
        # TODO Fix this, no tiene el id que se quiere editar o decide si lo buscas internamente                
        for entry in json_obj.keys():
            if entry not in PlayerHandler.player_dummy.__dict__.keys():
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:
                player: Player
                player = Player(**json_obj)                
                print(f'After the edit was made: {PlayerRepository().edit(player)}')
                return jsonify(Player=vars(PlayerRepository().get(player_id))), OK

    def delete(self, player_id):
        # Pending Revision
        player: Player
        player = PlayerRepository().get(player_id)
        PlayerRepository().delete(player_id)
        if player:
            return jsonify(Player=player.__dict__), OK
        else:
            return jsonify(Error='No Player found with that id.'), NOT_FOUND

    def get(self, player_id):
        players = PlayerDAO().get(player_id)
        if players:
            return jsonify(Players=[player.serialize() for player in players]), OK
        else:
            return jsonify(Error='No Player found with that id.'), NOT_FOUND

    def search(self, args: Dict):        
        # Pending Revision
        player_rep = PlayerRepository()        
        # try:
        return jsonify(player_rep.getPlayerByAttributes(args)), OK
        # except Exception as e:
            # print(e)
            # return jsonify(Error='Invalid player attributes for search.'), NOT_FOUND

    def compare_players(self, player_1, player_2):
        # Pending Revision
        # TODO do it mai dude
        pass


    def getAllPlayerSoccerStatistics(self):
        stats = SoccerPlayerStatisticDAO().getAll()
        return jsonify(SoccerPlayer=[stat.__dict__ for stat in stats]), OK

    def getSoccerPlayerStatisticById(self, statid):
        stats = SoccerPlayerStatisticDAO().get(statid)
        if stats:
            return jsonify(SoccerPlayer=[stat.__dict__ for stat in stats]), OK
        else:
            return jsonify(Error='No statistic found with that id.'), NOT_FOUND

    def addPlayerStatistic(self, json):
        if ('player_id' in json) and ('halve_number' in json) and ('goals_scored' in json) and ('assists' in json) and ('tackles_won' in json) and ('saves' in json) and ('passes_completed' in json) and ('yellow_cards' in json) and ('red_cards' in json) and ('year' in json):
            new_stat = SoccerPlayerStatistic(0, json['player_id'], json['halve_number'], json['goals_scored'], json['assists'], json['tackles_won'], json['saves'], json['passes_completed'], json['yellow_cards'], json['red_cards'], json['year'])
            playerStats = SoccerPlayerStatisticDAO().add(new_stat)
            return jsonify(SoccerPlayer=[stat.__dict__ for stat in playerStats]), CREATED
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST



