import mariadb
from dao.dummy_data import soccer_team_dummy_data, soccerStat_count
from soccerTeam.soccerTeamStatistics import SoccerTeam
from handler import utils
import psycopg2

class SoccerTeamDAO:

        def __init__(self):
            self.conn = utils.connectDB()


        def getAll(self):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, wins, draws, losses, goals_for, goals_allowed, goal_difference, points, year FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) ORDER BY team_id;"
            cursor.execute(query)
            result = cursor.fetchall()
            team = [teamStat for teamStat in result]
            return [SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        def getByid(self, statid):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, wins, draws, losses, goals_for, goals_allowed, goal_difference, points, year FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) where id = %s;"
            cursor.execute(query, [statid])
            teamStat = cursor.fetchone()
            return SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9])

        def getByTeamid(self, tid):
            self.conn = utils.connectDB()
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, wins, draws, losses, goals_for, goals_allowed, goal_difference, points, year FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE team_id = %s order by year;"
            cursor.execute(query, [tid])
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        #returns a teams statistics from that year (cant make the logic to recieve team_name right now is using team id)
        def getByTeamAndDate(self, team_name, year):
            cursor = self.conn.cursor()
            query = "SELECT soccer_team_statistics.id, team_id, wins, draws, losses, goals_for, goals_allowed, goal_difference, points, year FROM ((soccer_team_statistics JOIN team_sport ON team_sport_id = team_sport.id) JOIN team ON team_id = team.id) WHERE name = %s and year = %s;"
            cursor.execute(query, [team_name], year)
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        # returns all teams' statistics from that year ordered by teams
        def getByYear(self, year):
            cursor = self.conn.cursor()
            query = "select id, team_id, wins, draws, losses, goals_for, goals_allowed, goal_difference, points, year from soccer_team_statistics natural inner join team_sport where year = %s order by team_id;"
            cursor.execute(query, [year])
            team = cursor.fetchall()
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        # adds new entry for a team statistic
        def add(self, soccerTeam):
            cursor = self.conn.cursor()
            query = "INSERT INTO soccer_team_statistics(team_sport_id,wins,draws,losses,goals_for, goals_allowed, goal_difference, points, year) values(%s, %s, %s, %s, %s, %s, %s, %s) returning id;"
            cursor.execute(query, (soccerTeam.team_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.date))
            newTeamStat = SoccerTeam(soccerStat_count, soccerTeam.team_sport_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.year)
            return newTeamStat

        # deletes a team statistic record (search by year? or team?)
        def delete(self, statid):
            cursor = self.conn.cursor()
            query = "delete from soccer_team_statistics where statid = %s;"
            cursor.execute(query, [statid])
            return

        # edit a team statistic record
        def edit(self, soccerTeam):
            cursor = self.conn.cursor()
            query = "UPDATE soccer_team_statistics SET team_sport_id = %s, wins = %s, losses = %s, goals_for = %s, goals_allowed = %s, goal_difference = %s, points = %s, year = %s WHERE statid = %s;"
            cursor.execute(query, (soccerTeam.team_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for,soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.date, [soccerTeam.statid]))
            newTeamStat = SoccerTeam(soccerStat_count, soccerTeam.team_sport_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.year)
            return newTeamStat