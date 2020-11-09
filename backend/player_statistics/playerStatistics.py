from db_entity import DB_Entity

class PlayerStatistic(DB_Entity):
    def __init__(self, player_id, position, date, gamesPlayed):
        super(PlayerStatistic, self)
        self.player_id = player_id
        self.position = position
        self.date = date
        self.gamesPlayed = gamesPlayed