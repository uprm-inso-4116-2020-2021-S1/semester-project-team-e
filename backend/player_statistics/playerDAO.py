

from player_statistics.soccerPlayerStatistic import SoccerPlayerStatistic
from dao.dummy_data import soccer_dummy_data

class SoccerPlayerStatisticDAO():
    
    def getAll(self):
        return [ stat for stat in soccer_dummy_data ]

    def get(self, pid):
        return [ stat for stat in soccer_dummy_data if stat[0] == pid]

    def add(self, stat):
        pass

    def edit(self, stat, json_obj: Dict):
        pass

    def delete(self, stat):
        pass

class PlayerDAO:
    
    def get_all(self):
        pass

    def get(self, player_id):
        pass

    def add(self, player_info):
        pass

    def edit(self, player_info):
        pass

    def delete(self, player_id):
        pass