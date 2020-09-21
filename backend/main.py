from flask import Flask, request
from flask_cors import CORS

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
    # return UserHandler().login(request.json)
    return 'Login page'

# Team routes
@app.route('/team', methods = [GET, POST])
def addTeam():
    if request.method == POST:
        # return TeamHandler().add(request.json)
        return 'Add a new team'
    else:
        # return TeamHandler().getAll()
        return 'Get all teams'

@app.route('/team/<int: id>', methods = [GET, PUT, DELETE] )
def getTeamByID(id):
    if request.method == PUT:
        # return TeamHandler().edit(id, request.json)
        return 'Edit team by id'
    elif request.method == DELETE:
        # return TeamHandler().delete(id)
        return 'Delete team by id'
    else:
        # return TeamHandler().get(id)
        return 'Get team by id'

# Player routes
@app.route('/player', methods = [GET, POST])
def addPlayer():
    if request.method == POST:
        # return PlayerHandler().add(request.json)
        return 'Add a new player'
    else:
        # return PlayerHandler().getAll()
        return 'Get all players'

@app.route('/player<int: id', methods = [GET, PUT, DELETE])
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

