

from player_statistics.soccerPlayerStatistic import SoccerPlayerStatistic
from dao.dummy_data import soccer_dummy_data

class soccerPlayerStatisticDAO():
    
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