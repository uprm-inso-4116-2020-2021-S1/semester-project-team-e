from flask import Flask, request, json
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, jwt_required, jwt_optional, get_jwt_identity)
from team.teamHandler import TeamHandler
from player.playerHandler import PlayerHandler
from manager.managerHandler import ManagerHandler

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'unsafe-key'
CORS(app)
jwt = JWTManager(app)

DELETE = 'DELETE'
PUT = 'PUT'
POST = 'POST'
GET = 'GET'

@app.route('/home')
def home():
    return 'Home page'

# Register routes
@app.route('/register', methods = [POST])
def registerManager():
    return ManagerHandler().register(request.json)

@app.route('/register/player', methods = [POST])
def registerPlayer():
    # return PlayerHandler().register(request.json)
    return 'Register as a player'

# Login
@app.route('/login', methods = [POST])
def login():
    return ManagerHandler().login(request.json)

# Team routes
@app.route('/team', methods = [GET, POST])
@jwt_optional
def addTeam():
    manager = get_jwt_identity()
    if manager:
        if request.method == POST:
            return TeamHandler().add(request.json)
    else:
        if request.args:
            return TeamHandler().search(request.args)
        else:
            return TeamHandler().getAll()

@app.route('/team/<int:tid>', methods = [GET, PUT, DELETE])
@jwt_optional
def getTeamByID(tid):
    manager = get_jwt_identity()
    if manager:
        if request.method == PUT:
            return TeamHandler().edit(tid, request.json)
        elif request.method == DELETE:
            return TeamHandler().delete(tid)
    else:
        return TeamHandler().get(tid)

@app.route('/team/compare')
def compareTeam():
    return TeamHandler().compare(request.args)

# Player routes
@app.route('/player', methods = [GET, POST])
def addPlayer():
    if request.method == POST:
        return PlayerHandler().add(request.get_json())
    elif request.args:
        return PlayerHandler().search(request.args)
    else:
        return PlayerHandler().getAll()


@app.route('/player<int:id>', methods = [GET, PUT, DELETE])
def getPlayerByID(id):
    if request.method == PUT:
        return PlayerHandler().edit(request.get_json(), id)
    elif request.method == DELETE:
        return PlayerHandler().delete(id)
    elif request.args:
        return PlayerHandler().search(request.args)

    else:
        return PlayerHandler().get(id)


@app.route('/player/compare,<int:player_1>,<int:player_2>')
def comaprePlayer(player_1, player_2):
    # return PlayerHandler().compare(request.args)
    return PlayerHandler().compare_players(player_1, player_2)

@app.route('/player/soccer', methods = [GET, POST])
def getAllPlayerStatistics():
    if request.method == GET:
        return PlayerHandler().getAllPlayerSoccerStatistics()
    elif request.method == POST and request.args:
        return PlayerHandler().add(request.args)

@app.route('/player/soccer<int:stat_id>', methods = [GET, PUT, DELETE])
def getSoccerPlayerStatistic(stat_id):
    if request.method == GET:
        return PlayerHandler().getSoccerPlayerStatisticById(stat_id)
    elif request.method == PUT:
        # TODO implement
        return None
    elif request.method == DELETE:
        # TODO implement
        return None
#statistics routes
@app.route('/team/<int:tid>/statistics', methods=[POST])
def addTeamStatistics(tid):
    if request.method == POST:
        return TeamHandler().addTeamStat(tid, request.json)

@app.route('/teamstatistics/<int:statid>', methods=[PUT, DELETE])
def getTeamStatisticsByID(statid):
    if request.method == PUT:
        return TeamHandler().editTeamStat(statid, request.json)
    else:
        return TeamHandler().deleteTeamStat(statid)


#user routes
@app.route('/manager', methods = [GET])
def getUsers():
    return ManagerHandler().getAll()

@app.route('/manager/<int:userid>', methods = [GET, PUT, DELETE])
def getUserByID(userid):
    manager = get_jwt_identity()
    if manager:
        if request.method == PUT:
            return ManagerHandler().edit(userid, request.json)
        elif request.method == DELETE:
            return ManagerHandler().delete(userid)
    else:
        return ManagerHandler().get(userid)

@app.route('/manager/myteams', methods = [POST])
def getMyTeams():
    return ManagerHandler().getMyTeams(request.json)

#Team Records routes
@app.route('/teamrecord', methods = [POST])
def addTeamRecord():
    return TeamHandler().addTeamRecord(request.json)

@app.route('/teamrecord/<int:recordid>', methods = [PUT, DELETE])
def getTeamRecordByID(recordid):
    if request.method == PUT:
        return TeamHandler().editTeamRecord(recordid, request.json)
    else:
        return TeamHandler().deleteTeamRecord(recordid)

if __name__ == '__main__':
    app.run()

