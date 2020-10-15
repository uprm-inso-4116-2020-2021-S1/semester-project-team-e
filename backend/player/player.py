from player_statistics.playerStatistics import PlayerStatistic


class Player:
    
    def __init__(self, player_id=None, player_name=None, height=None, weight=None, team_name=None, sport_name=None, team_sport_id=None, sport_stats=None):
        self.player_id = player_id
        self.player_name = player_name
        self.height = height
        self.weight = weight
        self.team_name = team_name
        self.sport_name = sport_name 
        self.team_sport_id = team_sport_id
        if isinstance(sport_stats, PlayerStatistic):
            self.player_sport_stats = sport_stats.__dict__
        else:
            self.player_sport_stats = sport_stats


