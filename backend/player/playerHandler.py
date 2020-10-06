from typing import List, Dict
from player.player import Player
from player.playerRepository import PlayerRepository
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND

from flask import jsonify


class PlayerHandler:
    
    player_dummy = Player()

    def getAll(self):
        players: list
        players = []
        for player in PlayerRepository().getAll():
            players.append(player.__dict__)
        return jsonify(Players = players)     

    def add(self, json_obj: Dict):
        for entry in json_obj.keys():
            if entry not in PlayerHandler.player_dummy.__dict__.keys():
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:                
                player = Player(**json_obj)
                PlayerRepository().add(player)
                return jsonify(Player=player.__dict__), CREATED

    def edit(self, json_obj: Dict):
        for entryn in json_obj.keys():
            if entry not in PlayerHandler.player_dummy.__dict__.keys():
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:
                player: Player
                player = Player(**json_obj)
                player = PlayerRepository().edit(player)
                return jsonify(Player=player.__dict__), OK

    def delete(self, player_id):
        player: Player
        player = PlayerRepository().delete(player_id)
        if player:
            return jsonify(Player=player.__dict__), OK
        else:
            return jsonify(Error='No Player found with that id.'), NOT_FOUND

    def get(self, player_id):
        player: Player
        player = PlayerRepository().get(player_id)
        if player:
            return jsonify(Player=player.__dict__), OK
        else:
            return jsonify(Error='No Player found.'), NOT_FOUND

    def search(self, args: Dict):        
        player_rep = PlayerRepository()        
        try:
            return jsonify(player_rep.getPlayerByAttributes(args)), OK
        except:
            return jsonify(Error='Invalid player attributes for search.'), NOT_FOUND

        

