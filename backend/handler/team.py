from flask import jsonify
from handler.utils import CREATED, OK, BAD_REQUEST, NOT_FOUND
from dao.team import TeamDAO
from entitiy.team import Team
# from backend.team.services import compareTeam

class TeamHandler:
    def getAll(self):
        teams = TeamDAO().getAll()
        teams_list = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
        return jsonify(Teams = [ team.__dict__ for team in teams_list ]), OK

    def add(self, json):
        if json['team_name'] and json['team_info'] and json['sport_name']:
            teams = TeamDAO().add(json)
            team_obj = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
            return jsonify(Teams = [ team.__dict__ for team in team_obj ]), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def edit(self, tid, json):
        if json['team_name'] and json['team_info'] and json['sport_name']:
            teams = TeamDAO().edit(tid, json)
            team_obj = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
            return jsonify(Teams = [ team.__dict__ for team in team_obj ]), OK 
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def delete(self, tid):
        teams = TeamDAO().delete(tid)
        team_obj = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
        return jsonify(Teams = [ team.__dict__ for team in team_obj ]), OK

    def get(self, tid):
        teams = TeamDAO().get(tid)
        team_obj = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
        return jsonify(Teams = [ team.__dict__ for team in team_obj ]), OK

    #TODO: finish implementing
    def compare(self, args):
        team_id1 = args.get("id1")
        team_id2 = args.get("id2")
        # comparer = args.get("comparer")
        if team_id1 and team_id2: 
            team1_request = TeamDAO().get(team_id1)
            team2_request = TeamDAO().get(team_id2)
            team1 = [ Team(team[0], team[1], team[2], team[3]) for team in team1_request ]
            team2 = [ Team(team[0], team[1], team[2], team[3]) for team in team2_request ]
            # comparison = compareTeam(team1, team2) 
            comparison = {}
            return jsonify(comparison = comparison), OK
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def search(self, args):
        team_name = args.get("keyword")
        sport_name = args.get("sport_name")
        dao = TeamDAO()
        teams = []
        if (len(args) == 2) and team_name and sport_name:
            teams = dao.getByNameAndSport(team_name, sport_name)
        elif (len(args) == 1) and team_name:
            teams = dao.getByName(team_name)
        elif (len(args) == 1) and sport_name:
            teams = dao.getBySport(sport_name)
        else:
            return jsonify(Error = 'Malformed query string'), NOT_FOUND
        team_obj = [ Team(team[0], team[1], team[2], team[3]) for team in teams ]
        return jsonify(Teams = [ team.__dict__ for team in team_obj ]), OK