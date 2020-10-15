

from player_statistics.playerStatistic import PlayerStatistic

class SoccerPlayerStatistic(PlayerStatistic):
    def __init__(self, player_id=None, position=None, date=None, halve_number=None, games_played=None, saves=None, goals_scored=None, assists=None, tackles_won=None, passes_completed=None, red_cards=None, yellow_cards=None):
        super(self, SoccerPlayerStatistic).__init__(player_id, position, date, gamesPlayed)
        self.halve_number = halve_number
        self.saves = saves
        self.goalsScored = goalsScored
        self.assists = assists
        self.tacklesWon = tacklesWon
        self.passes_completed = passes_completed
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards