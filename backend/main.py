from flask import Flask, request, json
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, jwt_required, jwt_optional, get_jwt_identity)
from team.teamHandler import TeamHandler
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
        # return PlayerHandler().add(request.json)
        return 'Add a new player'
    elif request.args:
        # return PlayerHandler().search(request.args)
        return 'Search players by id'
    else:
        # return PlayerHandler().getAll()
        return 'Get all players'

@app.route('/player<int:tid>', methods = [GET, PUT, DELETE])
def getPlayerByID(id):
    if request.method == PUT:
        # return PlayerHandler().edit(id, request.json)
        return 'Edit player by id'
    elif request.method == DELETE:
        # return PlayerHandler().delete(id)
        return 'Delete player by id'
    else:
        # return PlayerHandler.get(id)
        return 'Get player by id'

@app.route('/player/compare')
def comaprePlayer():
    # return PlayerHandler().compare(request.args)
    return 'Compare two player'

#statistics routes
@app.route('/teamstatistics', methods=[POST])
def addTeamStatistics():
    if request.method == POST:
        return TeamHandler().addTeamStat(request.json)

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
    if request.method == PUT:
        return ManagerHandler().edit(userid, request.json)
    elif request.method == DELETE:
        return ManagerHandler().delete(userid)
    else:
        return ManagerHandler().get(userid)

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

