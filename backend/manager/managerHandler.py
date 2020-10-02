from flask import jsonify
from handler.utils import OK, BAD_REQUEST, CREATED
from passlib.hash import sha256_crypt
from manager.managerRepository import ManagerRepository
from manager.manager import Manager

class ManagerHandler:
    def register(self, json):
        if json['username'] and json['email'] and json['password']:
            if not ManagerRepository().get(json['username']):
                json['password'] = sha256_crypt.hash(json['password']) 
                new_manager = Manager(0, json['username'], json['email'], json['password'])
                manager = ManagerRepository().add(new_manager)
                return jsonify(isAuth = True, UserID = manager.user_id, Username = manager.username), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST
        pass

    def login(self, json):
        if json['username'] and json['password']:
            manager = ManagerRepository().get(json['username'])
            if sha256_crypt.verify(json['password'], manager.password):
                return jsonify(IsAuth = True, UserID = manager.user_id, Username = manager.username), OK
            else:
                return jsonify(IsAuth = False), OK
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST
