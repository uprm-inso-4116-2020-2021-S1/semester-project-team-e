import json
from typing import List, Dict
from player.player import Player
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from player.playerRepository import PlayerRepository
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND

from flask import jsonify


class PlayerHandler:
    
    player_dummy = Player()

    def getAll(self):
        # Pending Revision
        players: list
        players = []        
        for player in PlayerRepository().getAll():
            players.append(player)
        return jsonify(Players = PlayerRepository().getAll())     

    def add(self, json_obj: Dict):
        # Pending Revision
        for entry in json_obj.keys():
            if entry not in PlayerHandler.player_dummy.__dict__.keys():
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:                
                player = Player(**json_obj)
                PlayerRepository().add(player)
                return jsonify(Player=player.__dict__), CREATED

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
        # Pending Revision
        player: Player
        player = PlayerRepository().get(player_id)
        if player:
            return jsonify(Player=player.__dict__), OK
        else:
            return jsonify(Error='No Player found.'), NOT_FOUND

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
        # Pending Revision
        player_individual_stats = PlayerRepository().getAllPlayerStatistics()
        print(player_individual_stats)
        for idx, item in enumerate(player_individual_stats):
            item: SoccerPlayerStatistic
            player_individual_stats[idx] = item.to_dictionary()
            
        return jsonify(SoccerPlayerStatistic = player_individual_stats), OK

    def getSoccerPlayerStatisticById(self, id):
        #  Pending Revision
        player_stat: SoccerPlayerStatistic
        player_stat = PlayerRepository().getPlayerStatById(id)
        if player_stat:
            return jsonify(SoccerPlayerStatistic = player_stat.to_dictionary()), OK
        else:
            return jsonify(Error = 'No player found by that id.'), NOT_FOUND


