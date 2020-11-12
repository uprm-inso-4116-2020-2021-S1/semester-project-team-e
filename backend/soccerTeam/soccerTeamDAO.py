from soccerTeam.soccerTeamStatistics import SoccerTeam
from handler import utils

class SoccerTeamDAO:

        def __init__(self):
            self.conn = utils.connectDB()


        def getAll(self):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM soccer_team_statistics ORDER BY team_id;"
            cursor.execute(query)
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        def getByid(self, statid):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM soccer_team_statistics where id = %s;"
            cursor.execute(query, [statid])
            teamStat = cursor.fetchone()
            return SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10])

        def getByTeamid(self, tid):
            self.conn = utils.connectDB()
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE team_id = %s ORDER BY date;"
            cursor.execute(query, [tid])
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        #returns a teams statistics from that year (cant make the logic to recieve team_name right now is using team id)
        def getByTeamAndDate(self, team_name, date):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE team.team_name = %s AND date = %s;"
            cursor.execute(query, [team_name], [date])
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        # returns all teams' statistics from that year ordered by teams
        def getByYear(self, date):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE date = %s;"
            cursor.execute(query, [date])
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9], teamStat[10]) for teamStat in team]

        # adds new entry for a team statistic and returns its statid
        def add(self, soccerTeam):
            cursor = self.conn.cursor()
            query = "INSERT INTO soccer_team_statistics(team_sport_id, goals_for, goals_allowed, shots, shots_on_goal, saves, passes, possession, fouls, date) values(%s, %s, %s, %s, %s, %s, %s, %s) returning id;"
            result = cursor.execute(query, (soccerTeam.team_id, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.shots, soccerTeam.shots_on_goal, soccerTeam.saves, soccerTeam.passes, soccerTeam.possession, soccerTeam.fouls, soccerTeam.date))
            return result

        # deletes a team statistic record (search by year? or team?)
        def delete(self, statid):
            cursor = self.conn.cursor()
            query = "DELETE FROM soccer_team_statistics WHERE id = %s;"
            cursor.execute(query, [statid])
            return

        # edit a team statistic record
        def edit(self, soccerTeam):
            cursor = self.conn.cursor()
            query = "UPDATE soccer_team_statistics SET team_sport_id = %s, goals_for = %s, goals_allowed = %s, shots = %s, shots_on_goal = %s, saves = %s, passes = %s, possession = %s, fouls = %s, date = %s WHERE id = %s;"
            cursor.execute(query, (soccerTeam.team_id, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.shots, soccerTeam.shots_on_goal, soccerTeam.saves, soccerTeam.passes, soccerTeam.possession, soccerTeam.fouls, soccerTeam.date, [soccerTeam.statid]))
            return