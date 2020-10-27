from flask import jsonify
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND
from team.teamRepository import TeamRepository
from team.team import Team
from team.teamServices import TeamService
from handler.utils import intoJSON
# from backend.team.services import compareTeam

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
        team = TeamRepository().get(tid)
        return jsonify(Teams = team.serialize()), OK

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

    def compare(self, args):
        tid1 = int(args.get("team1"))
        tid2 = int(args.get("team2"))
        if tid1 and tid2:
            comparison = TeamService.comparison(tid1, tid2)
            return jsonify(Comparison = comparison), OK
        else:
            return jsonify(Error = 'Malformed query string'), NOT_FOUND
