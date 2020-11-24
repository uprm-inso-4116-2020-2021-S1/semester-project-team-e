from team.teamRepository import TeamRepository
SOCCER_COMPATISON_STAT_FORMAT = ['statid', 'team_id', 'goals_for', 'goals_allowed', 'shots', 'shots_on_goal', 'saves', 'passes', 'possession', 'fouls', 'date']

class TeamService:
    @staticmethod
    def comparison(tid1, tid2):
        #Percent of statistics of all stat for team
        stats1 = TeamRepository().getAvgStats(tid1)
        stats2 = TeamRepository().getAvgStats(tid2)
        comulative_statistics_team1 = dict(zip(SOCCER_COMPATISON_STAT_FORMAT, stats1))
        comulative_statistics_team2 = dict(zip(SOCCER_COMPATISON_STAT_FORMAT, stats2))

        #Most favored to win
        points = {'t1':0, 't2':0}
        for i in range(len(stats1)):
            if stats1[i] > stats2[i]:
                points['t1'] += 1
            else:
                points['t2'] += 1

        most_favored = 'team1' if points['t1'] > points['t2'] else 'team2'

        # TODO: compare using possession, goals scored, shot and past results.
        return {'average_stats_team1' : comulative_statistics_team1, 'average_stats_team2' : comulative_statistics_team2, 'most_favored' : most_favored}

    @staticmethod
    def Ranker():
        pass