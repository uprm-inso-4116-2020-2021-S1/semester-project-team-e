from flask import jsonify
from handler.utils import to_specified_format, CREATED, OK, BAD_REQUEST
from entity.team import Team

TEAM_FORMAT = []

class TeamHandler:
    def getAll(self):
        teams = TeamDAO().getAll()
        teams_list = to_specified_format(teams, TEAM_FORMAT)
        return jsonify(Administrators = teams_list), OK

    #TODO
    def add(self, request):
        return

    #TODO
    def edit(self, id, request):
        return

    #TODO
    def delete(self, id):
        return

    #TODO
    def get(self, id):
        team = TeamDAO().get(id)
        team_obj = Team(team[0], team[1], team[2], team[3])
        return team_obj

    
