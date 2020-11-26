from flask import jsonify
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND
from team.teamRepository import TeamRepository
from team.team import Team
from team.teamServices import TeamService
from handler.utils import intoJSON
from soccerTeam.soccerTeamStatistics import SoccerTeam
# from backend.team.services import compareTeam
from soccerTeam.soccerTeamDAO import SoccerTeamDAO
from Records.teamRecords import TeamRecords
from Records.recordsDAO import RecordsDAO
from soccerTeam.TeamSpecificationPattern import SoccerTeamSpecification


class TeamHandler:

    def getAll(self):
        teams = TeamRepository().getAll()
        validTeams = list()
        for team in teams:
            if SoccerTeamSpecification().isValidTeam(team):
                validTeams.append(team)
            else:
                pass
        return jsonify(Teams = [ team.serialize() for team in validTeams ]), OK
        # return jsonify(Teams=[team.serialize() for team in teams]), OK

    def add(self, json):
        if json['username'] and json['team_name'] and json['team_info'] and json['sport_name']:
            new_team = Team(0, json['team_name'], json['team_info'], json['sport_name'])
            teams = TeamRepository().add(new_team, json['username'])
            return jsonify(Teams=[team.serialize() for team in teams]), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def edit(self, tid, json):
        if tid and json['team_name'] and json['team_info'] and json['sport_name']:
            new_team = Team(tid, json['team_name'], json['team_info'], json['sport_name'])
            teams = TeamRepository().edit(new_team)
            return jsonify(Teams=[team.serialize() for team in teams]), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def delete(self, tid):
        teams = []
        teams = TeamRepository().delete(tid)
        return jsonify(Teams=[team.serialize() for team in teams]), OK

    def get(self, tid):
        teams = TeamRepository().get(tid)
        validTeams = list()
        for team in teams:
            if SoccerTeamSpecification().isValidTeam(team):
                validTeams.append(team)
            else:
                pass
        return jsonify(Teams=[team.serialize() for team in validTeams]), OK
        # return jsonify(Teams = [ team.serialize() for team in teams ]), OK

    def search(self, args):
        team_name = args.get("keyword")
        sport_name = args.get("sport_name")
        repository = TeamRepository()
        teams = []
        if (len(args) == 2) and team_name and sport_name:
            teams = repository.getByNameAndSport(team_name, sport_name)
        elif (len(args) == 1) and team_name:
            teams = repository.getByName(team_name)
        elif (len(args) == 1) and sport_name:
            teams = repository.getBySport(sport_name)
        else:
            return jsonify(Error='Malformed query string'), NOT_FOUND
        validTeams = list()
        for team in teams:
            if SoccerTeamSpecification().isValidTeam(team):
                validTeams.append(team)
            else:
                pass
        return jsonify(Teams=[team.serialize() for team in validTeams]), OK
        # return jsonify(Teams = [ team.serialize() for team in teams ]), OK


    def compare(self, args):
        tid1 = int(args.get("team1"))
        tid2 = int(args.get("team2"))
        if tid1 and tid2:
            comparison = TeamService.comparison(tid1, tid2)
            return jsonify(Comparison = comparison), OK
        else:
            return jsonify(Error = 'Malformed query string'), NOT_FOUND

    def addTeamStat(self, tid, json):                                                                                        #only team statistic part json, only works for 1 sport, have to incorporate team statistic factory for more sports
        print(json)
        # if json['goals_for'] and json['goals_allowed'] and json['shots'] and json['shots_on_goal'] and json['saves'] and json['passes'] and json['possession'] and json['fouls'] and json['date']:
        if ('goals_for' in json) and ('goals_allowed' in json) and ('shots' in json) and ('shots_on_goal' in json) and ('saves' in json) and ('passes' in json) and ('possession' in json) and ('date' in json):
            new_teamStat = SoccerTeam(0, tid, json['goals_for'], json['goals_allowed'], json['shots'], json['shots_on_goal'], json['saves'], json['passes'], json['possession'], json['fouls'], json['date'])
            if json['match_result'] == 'win':
                wld = 0
                stat = SoccerTeamDAO().add(new_teamStat, wld)
            elif json['match_result'] == 'loss':
                wld = 1
                stat = SoccerTeamDAO().add(new_teamStat, wld)
            else:
                wld = 2
                stat = SoccerTeamDAO().add(new_teamStat, wld)
            return jsonify(SoccerTeam=stat.__dict__), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def deleteTeamStat(self, statid):
        stat = SoccerTeamDAO().delete(statid)
        return jsonify(SoccerTeam=stat.__dict__), OK

    def editTeamStat(self, statid, json):
        if statid and json['team_id'] and json['goals_for'] and json['goals_allowed'] and json['shots'] and json['shots_on_goal'] and json['saves'] and json['passes'] and json['possession'] and json['fouls'] and json['date']:
            new_teamStat = SoccerTeam(statid, json['team_id'], json['goals_for'], json['goals_allowed'], json['shots'], json['shots_on_goal'], json['saves'], json['passes'], json['possession'], json['fouls'], json['date'])
            stat = SoccerTeamDAO().edit(new_teamStat)
            return jsonify(SoccerTeam=stat.__dict__), OK
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST

    def addTeamRecord(self, json):
        if json['team_id'] and json['wins'] and json['loss'] and json['draw'] and json['year']:
                new_teamRecord = TeamRecords(0, json['team_id'], json['wins'], json['loss'], json['draw'], json['year'])
                record = RecordsDAO().add(new_teamRecord)
                return jsonify(TeamRecords=record.__dict__), OK
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST

    def editTeamRecord(self, recordid, json):
        if json['team_id'] and json['wins'] and json['loss'] and json['draw'] and json['year']:
                new_teamRecord = TeamRecords(recordid, json['team_id'], json['wins'], json['loss'], json['draw'], json['year'])
                record = RecordsDAO().edit(new_teamRecord)
                return jsonify(TeamRecords=record.__dict__), OK
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST

    def deleteTeamRecord(self, recordid):
        record = RecordsDAO().delete(recordid)
        return jsonify(TeamRecords=record.__dict__), OK