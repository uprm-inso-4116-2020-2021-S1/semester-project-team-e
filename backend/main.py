from flask import Flask, request, json
from flask_cors import CORS
from team.teamHandler import TeamHandler
from player.playerHandler import PlayerHandler


app = Flask(__name__)
CORS(app)

DELETE = 'DELETE'
PUT = 'PUT'
POST = 'POST'
GET = 'GET'

@app.route('/home')
def home():
    return 'Home page'

# Register routes
@app.route('/register/manager', methods = [POST])
def registerManager():
    # return ManagerHandler().register(request.json)
    return 'Register as a manager'

@app.route('/register/player', methods = [POST])
def registerPlayer():
    # return PlayerHandler().register(request.json)
    return 'Register as a player'

# Login
@app.route('/login', methods = [POST])
def login():
    return User().login(request.json)

# Team routes
@app.route('/team', methods = [GET, POST])
def addTeam():
    if request.method == POST:
        return TeamHandler().add(request.json)
    elif request.args:
        return TeamHandler().search(request.args)
    else:
        return TeamHandler().getAll()

@app.route('/team/<int:tid>', methods = [GET, PUT, DELETE] )
def getTeamByID(tid):
    if request.method == PUT:
        return TeamHandler().edit(tid, request.json)
    elif request.method == DELETE:
        return TeamHandler().delete(tid)
    else:
        return TeamHandler().get(tid)

@app.route('/team/compare')
def compareTeam():
    # return TeamHandler().compare(request.args)
    return 'Compare two teams'

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
    else:
        return PlayerHandler().get(id)
        

@app.route('/player/compare,<int:player_1>,<int:player_2>')
def comaprePlayer():
    # return PlayerHandler().compare(request.args)
    return PlayerHandler().compare_players(player_1, player_2)

