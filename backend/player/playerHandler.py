import json
from typing import List, Dict
from player.player import Player
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from player.playerRepository import PlayerRepository
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND

from flask import jsonify


class PlayerHandler:
    
    def getAll(self):        
        players = []
        players_id = PlayerRepository()._getAllPlayerIds()
        print(players_id)
        if players_id:
            for p_id in players_id:
                print(p_id)
                plyr = PlayerRepository().getPlayerAndStats(p_id)
                if plyr:
                    players.append(plyr)        
        return jsonify(Players = players)     

    def add(self, json_obj: Dict):        
        for entry in json_obj.keys():
            if entry not in Player.PLAYER_DB_ADD_FORMAT:
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:
                return jsonify(Player_Id=PlayerRepository().addPlayer(json_obj)), CREATED

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
        player: Player
        player = PlayerRepository().getPlayerByID(player_id)        
        if player:
            PlayerRepository().deletePlayer(player_id)
            return jsonify(Player=player), OK
        else:
            return jsonify(Error='No Player found with that id.'), NOT_FOUND

    def get(self, player_id):
        player: Player
        player = PlayerRepository().getPlayerAndStats(player_id)
        if player:
            return jsonify(Player=player), OK
        else:
            return jsonify(Error='No Player found.'), NOT_FOUND

    def search(self, args: dict):        
        ''' Only searches for a player that has any attribute provided ''' 
        player_rep = PlayerRepository()                
        results = player_rep.getPlayerByAttributes(args)
        if results:
            return jsonify(Player=results), OK
        else:
            return jsonify(Error='No player found...'), NOT_FOUND
    
    def getAllPlayerSoccerStatistics(self):
        ''' Gets all players individual soccer statistics '''
        player_individual_stats = PlayerRepository().getAllPlayerStatistics()
        return jsonify(SoccerPlayerStatistic = player_individual_stats), OK

    def getSoccerPlayerStatisticById(self, id):
        ''' Gets soccer player stat by given id ''' 
        player_stat: SoccerPlayerStatistic
        player_stat = PlayerRepository().getPlayerStatById('soccer', id)
        if player_stat:
            return jsonify(SoccerPlayerStatistic = player_stat), OK
        else:
            return jsonify(Error = 'No player found by that id.'), NOT_FOUND


    