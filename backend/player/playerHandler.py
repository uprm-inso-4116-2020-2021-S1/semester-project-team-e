import json
from typing import List, Dict
from player.player import Player
from player_statistics.soccerPlayerStatistics import SoccerPlayerStatistic
from player.playerRepository import PlayerRepository
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND, CONFLICT

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
        for entry in json_obj.keys():
            if entry not in Player.PLAYER_DB_FORMAT:
                return jsonify(Error='Unexpected attributes in post.'), BAD_REQUEST
            else:
                player = json_obj                                
                PlayerRepository().editPlayer(json_obj)
                updated_player = PlayerRepository().getPlayerByID(player_id)
                if updated_player:
                    return jsonify(Player=updated_player), OK
                else:
                    return jsonify(Error='Can\'t verify the updated ocurred.'), NOT_FOUND
        return jsonify(Error='Could not complete operation.'), CONFLICT

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

    def getPlayerStatisticById(self, player_id):
        try:
            return jsonify(PlayerStatistic=PlayerRepository().getPlayerStatisticsByPlayerId(player_id)), OK
        except:
            return jsonify(Error='Could not complete requested action.'), CONFLICT



    