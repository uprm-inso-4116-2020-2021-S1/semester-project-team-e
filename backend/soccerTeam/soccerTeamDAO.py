# import mariadb
from dao.dummy_data import soccer_team_dummy_data, soccerStat_count
from soccerTeam.soccerTeamStatistics import SoccerTeam

class SoccerTeamDAO:

        def __init__(self):
            # self.conn = generic_db_connect()
            pass

        def getAll(self):
            return [SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in soccer_team_dummy_data]

        def getByid(self, statid):
            teamStat = [teamStat for teamStat in soccer_team_dummy_data if teamStat[0] == statid]
            return SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9])

        def getByTeamid(self, tid):
            team = [teamStat for teamStat in soccer_team_dummy_data if teamStat[1] == tid]
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        #returns a teams statistics from that year (cant make the logic to recieve team_name right now is using team id)
        def getByTeamAndDate(self, team_name, year):
            team = [teamStat for teamStat in soccer_team_dummy_data if teamStat[1] == team_name and teamStat[9] == year]
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        # returns all teams statistics from that year
        def getByYear(self, year):
            team = [teamStat for teamStat in soccer_team_dummy_data if teamStat[9] == year]
            return [ SoccerTeam(teamStat[0], teamStat[1], teamStat[2], teamStat[3], teamStat[4], teamStat[5], teamStat[6], teamStat[7],teamStat[8], teamStat[9]) for teamStat in team]

        # adds new entry for a team statistic
        def add(self, soccerTeam):
            newTeamStat = SoccerTeam(soccerStat_count, soccerTeam.team_sport_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.year)
            return newTeamStat

        # deletes a team statistic record (search by year? or team?)
        def delete(self, statid):
            return

        # edit a team statistic record
        def edit(self, soccerTeam):
            newTeamStat = SoccerTeam(soccerStat_count, soccerTeam.team_sport_id, soccerTeam.wins, soccerTeam.draw, soccerTeam.losses, soccerTeam.goals_for, soccerTeam.goals_allowed, soccerTeam.goal_difference, soccerTeam.points, soccerTeam.year)
            return newTeamStat