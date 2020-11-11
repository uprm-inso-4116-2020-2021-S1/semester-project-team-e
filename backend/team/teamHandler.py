from flask import jsonify
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND
from team.teamRepository import TeamRepository
from team.team import Team
from handler.utils import intoJSON
from soccerTeam.soccerTeamStatistics import SoccerTeam
# from backend.team.services import compareTeam
from soccerTeam.soccerTeamDAO import SoccerTeamDAO


class TeamHandler:

    def getAll(self):
        teams = TeamRepository().getAll()
        return jsonify(Teams = [ team.serialize() for team in teams ]), OK

    def add(self, json):
        if json['team_name'] and json['team_info'] and json['sport_name']:
            new_team = Team(0, json['team_name'], json['team_info'], json['sport_name'])
            team = TeamRepository().add(new_team)
            return jsonify(Team = team.serialize()), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def edit(self, tid, json):
        if json['team_name'] and json['team_info'] and json['sport_name']:
            new_team = Team(tid, json['team_name'], json['team_info'], json['sport_name'])
            team = TeamRepository().edit(new_team)
            return jsonify(Teams = team.serialize()), OK 
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def delete(self, tid):
        team = TeamRepository().delete(tid)
        return jsonify(Teams = team.serialize()), OK

    def get(self, tid):
        teams = TeamRepository().get(tid)
        return jsonify(Teams = [ team.serialize() for team in teams ]), OK

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
            return jsonify(Error = 'Malformed query string'), NOT_FOUND
        return jsonify(Teams = [ team.serialize() for team in teams ]), OK


    def addTeamStat(self, json):                                                                                        #only team statistic part json
        if json['team_id'] and json['goals_for'] and json['goals_allowed'] and json['shots'] and json['shots_on_goal'] and json['saves'] and json['passes'] and json['possession'] and json['fouls'] and json['date']:
            new_teamStat = SoccerTeam(0, json['team_id'], json['goals_for'], json['goals_allowed'], json['shots'], json['shots_on_goal'], json['saves'], json['passes'], json['possession'], json['fouls'], json['date'])
            stat = SoccerTeamDAO().add(new_teamStat)
            return jsonify(SoccerTeam = stat.__dict__), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def deleteTeamStat(self, statid):
        stat = SoccerTeamDAO().delete(statid)
        return jsonify(SoccerTeam=stat.__dict__), OK

    def editTeamStat(self, statid, json):
        if json['team_id'] and json['goals_for'] and json['goals_allowed'] and json['shots'] and json['shots_on_goal'] and json['saves'] and json['passes'] and json['possession'] and json['fouls'] and json['date']:
            new_teamStat = SoccerTeam(statid, json['team_id'], json['goals_for'], json['goals_allowed'], json['shots'], json['shots_on_goal'], json['saves'], json['passes'], json['possession'], json['fouls'], json['date'])
            stat = SoccerTeamDAO().edit(new_teamStat)
            return jsonify(SoccerTeam=stat.__dict__), OK
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST