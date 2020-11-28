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
        cursor.close()
        self.conn.close()
        return records_obj

    def get(self, recordid):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE team_records.id = ?"
        cursor.execute(query, (recordid,))
        record = cursor.fetchone()
        cursor.close()
        return TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5])

    def getbyyear(self, year):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE year = ? ORDER BY team_id"
        cursor.execute(query, (year,))
        result = cursor.fetchall()
        records_tup = [record for record in result]
        records_obj = [TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5]) for record in records_tup]
        cursor.close()
        self.conn.close()
        return records_obj

    def getByTeamID(self, teamid):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id, team_id, win, loss, draw, year FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE team_id = ? ORDER BY year"
        cursor.execute(query, (teamid,))
        result = cursor.fetchall()
        records_tup = [record for record in result]
        records_obj = [TeamRecords(record[0], record[1], record[2], record[3], record[4], record[5]) for record in records_tup]
        cursor.close()
        self.conn.close()
        return records_obj

    def getByTeamIDAndYear(self, teamid, year):
        cursor = self.conn.cursor()
        query = "SELECT team_records.id FROM (team_records JOIN team_sport ON teamSportID = team_sport.id) WHERE year = ? AND team_id = ?"
        cursor.execute(query, (year, teamid,))
        record = cursor.fetchone()[0]
        cursor.close()
        self.conn.close()
        if record == None:
            return False
        else:
            return record

    def add(self, teamRecords):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "SELECT id FROM team_sport WHERE team_id = ?"
        cursor.execute(query, (teamRecords.team_id,))
        team_sportid = cursor.fetchone()[0]
        query1 = "INSERT INTO team_records(teamSportID, win, loss, draw, year) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(query1, (team_sportid, teamRecords.wins, teamRecords.loss, teamRecords.draw, teamRecords.year,))
        record_id = cursor.lastrowid
        records_obj = self.get(record_id)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return records_obj

    def delete(self, recordid):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        result = self.get(recordid)
        query = "DELETE FROM team_records WHERE id = ?"
        cursor.execute(query, (recordid,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return result

    def edit(self, TeamRecords):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query1 = "UPDATE team_records SET win = ?, loss = ?, draw = ?, year = ? WHERE id = ?"
        cursor.execute(query1, (TeamRecords.wins, TeamRecords.loss, TeamRecords.draw, TeamRecords.year, TeamRecords.records_id,))
        records_obj = self.get(TeamRecords.records_id)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return records_obj

    def addWinToRecord(self, recordid):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "UPDATE team_records SET win = win + 1 WHERE id = ?"
        cursor.execute(query, (recordid,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return

    def addLossToRecord(self, recordid):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "UPDATE team_records SET loss = loss + 1 WHERE id = ?"
        cursor.execute(query, (recordid,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return

    def addDrawToRecord(self, recordid):
        self.conn = utils.connectDB()
        cursor = self.conn.cursor()
        query = "UPDATE team_records SET draw = draw + 1 WHERE id = ?"
        cursor.execute(query, (recordid,))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return