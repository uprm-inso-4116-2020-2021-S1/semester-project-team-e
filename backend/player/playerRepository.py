from flask import jsonify
from player.player import Player
from dao.dummy_data import player_dat




class PlayerRepository:
    
    def getAll(self):
        return [Player(**player_info) for player_info in player_dat]
        

    def get(self, player_id):        
        player = [player for player in player_dat if player['player_id'] == player_id]
        if player:
            return Player(**player[0])
        else:
            return None

    def add(self):
        return Player(**player_dat[2])


    def edit(self):
        return Player(**player_dat[1])

    def delete(self):
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