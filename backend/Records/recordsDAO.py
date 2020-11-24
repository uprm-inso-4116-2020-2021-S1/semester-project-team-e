from handler import utils
from Records.teamRecords import TeamRecords

class RecordsDAO:

    def __init__(self):
        self.conn = utils.connectDB()

    def getall(self):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id)"
        cursor.execute(query)
        result = cursor.fetchall()
        records_tup = [record for record in result]
        records_obj = [TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5]) for record in records_tup]
        return records_obj

    def get(self, recordid):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE team_records.id = ?"
        cursor.execute(query, (recordid,))
        record = cursor.fetchone()
        return TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5])

    def getbyyear(self, year):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE year = ? ORDER BY team_id"
        cursor.execute(query, (year,))
        result = cursor.fetchall()
        records_tup = [record for record in result]
        records_obj = [TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5]) for record in records_tup]
        return records_obj

    def getByTeamID(self, teamid):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE team_id = ? ORDER BY year"
        cursor.execute(query, (teamid,))
        result = cursor.fetchall()
        records_tup = [record for record in result]
        records_obj = [TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5]) for record in records_tup]
        return records_obj

    def add(self, teamRecords):
        cursor = self.conn.cursor()
        query = "SELECT id FROM team_sport WHERE team_id = ?"
        cursor.execute(query, (teamRecords.team_id,))
        team_sportid = cursor.fetchone()[0]
        query1 = "INSERT INTO team_records(teamSportID, win, loss, draw, year) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(query1, (team_sportid, teamRecords.wins, teamRecords.loss, teamRecords.draw, teamRecords.year,))
        record_id = cursor.lastrowid
        records_obj = self.get(record_id)
        self.conn.commit()
        return records_obj

    def delete(self, recordid):
        cursor = self.conn.cursor()
        result = self.get(recordid)
        query = "DELETE FROM team_records WHERE id = ?"
        cursor.execute(query, (recordid,))
        self.conn.commit()
        return result

    def edit(self, TeamRecords):
        cursor = self.conn.cursor()
        query1 = "UPDATE team_records SET win = ?, loss = ?, draw = ?, year = ? WHERE id = ?"
        cursor.execute(query1, (TeamRecords.wins, TeamRecords.loss, TeamRecords.draw, TeamRecords.year, TeamRecords.records_id,))
        records_obj = self.get(TeamRecords.records_id)
        self.conn.commit()
        return records_obj
