

from player_statistics.playerStatistic import PlayerStatistic

class SoccerPlayerStatistic(PlayerStatistic):
    def __init__(self, player_id=None, position=None, date=None, halveNumber=None, gamesPlayed=None, saves=None, goalsScored=None, assists=None, tacklesWon=None, passesCompleted=None, redCards=None, yellowCards=None):
        super(self, SoccerPlayerStatistic).__init__(player_id, position, date, gamesPlayed)
        self.halveNumber = halveNumber
        self.saves = saves
        self.goalsScored = goalsScored
        self.assists = assists
        self.tacklesWon = tacklesWon
        self.passesCompleted = passesCompleted
        self.redCards = redCards
        self.yellowCards = yellowCards