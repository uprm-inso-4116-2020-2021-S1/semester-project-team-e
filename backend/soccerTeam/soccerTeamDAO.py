from soccerTeam.soccerTeamStatistics import SoccerTeam
from handler import utils

class SoccerTeamDAO:

        def __init__(self):
            self.conn = utils.connectDB()


        def getAll(self):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM (soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) ORDER BY team_id"
            cursor.execute(query)
            result = cursor.fetchall()
            stat_tup = [stat for stat in result]
            stat_obj = [SoccerTeam(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7],stat[8], stat[9], stat[10]) for stat in stat_tup]
            return stat_obj

        def get(self, statid):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM (soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) WHERE soccer_team_statistics.id = ?"
            cursor.execute(query, (statid,))
            teamStat = cursor.fetchone()
            print(teamStat)
            return SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10])

        def getByTeamid(self, tid):
            self.conn = utils.connectDB()
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM (soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) WHERE team_id = ? ORDER BY date;"
            cursor.execute(query, (tid,))
            stats = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in stats]

        #returns a teams statistics from that year (cant make the logic to recieve team_name right now is using team id)
        def getByTeamAndDate(self, team_name, date):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE team.team_name = ? AND date = ?"
            cursor.execute(query, (team_name, date,))
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        # returns all teams' statistics from that year ordered by teams
        def getByDate(self, date):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM (soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) WHERE date = ?"
            cursor.execute(query, (date,))
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        # adds new entry for a team statistic and returns its statid
        def add(self, soccerTeam):
            cursor = self.conn.cursor()

            query = "SELECT id FROM team_sport WHERE team_id = ?"
            cursor.execute(query, (soccerTeam.team_id,))
            team_sportid = cursor.fetchone()[0]
            query1 = "INSERT INTO soccer_team_statistics(team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query1, (team_sportid, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.shots, soccerTeam.shots_on_goal, soccerTeam.saves, soccerTeam.passes, soccerTeam.possession, soccerTeam.fouls, soccerTeam.date,))
            statid = cursor.lastrowid
            stat_obj = self.get(statid)
            self.conn.commit()
            return stat_obj

        # deletes a team statistic record (search by year? or team?)
        def delete(self, statid):
            cursor = self.conn.cursor()
            result = self.get(statid)
            query = "DELETE FROM soccer_team_statistics WHERE id = ?"
            cursor.execute(query, (statid,))
            self.conn.commit()
            return result

        # edit a team statistic record
        def edit(self, soccerTeam):
            cursor = self.conn.cursor()
            query = "UPDATE soccer_team_statistics SET goals_for = ?, goals_allowed = ?, shots = ?, shots_on_goal = ?, saves = ?, passes = ?, possession = ?, fouls = ?, date = ? WHERE id = ?"
            cursor.execute(query, (soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.shots, soccerTeam.shots_on_goal, soccerTeam.saves, soccerTeam.passes, soccerTeam.possession, soccerTeam.fouls, soccerTeam.date, soccerTeam.statid,))
            result = self.get(soccerTeam.statid)
            self.conn.commit()
            return result