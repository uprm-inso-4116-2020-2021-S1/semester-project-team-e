from db_entity import DB_Entity

class PlayerStatistic(DB_Entity):
    def __init__(self, player_id, position, date, games_played):
        super(PlayerStatistic, self)
        self.player_id = player_id
        self.position = position
        self.date = date
        self.games_played = games_played