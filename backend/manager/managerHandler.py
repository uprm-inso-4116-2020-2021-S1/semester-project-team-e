from flask import jsonify
from handler.utils import OK, BAD_REQUEST, CREATED, NOT_FOUND
from passlib.hash import sha256_crypt
from manager.managerRepository import ManagerDAO
from manager.manager import Manager
from flask_jwt_extended import create_access_token

class ManagerHandler:
    def register(self, json):
        if json['username'] and json['email'] and json['password'] and json['full_name']:
            if not ManagerDAO().getByUsername(json['username']):
                json['password'] = sha256_crypt.hash(json['password']) 
                new_manager = Manager(0, json['username'], json['password'], json['full_name'], json['email'])
                manager = ManagerDAO().add(new_manager)
                return jsonify(isAuth = True, UserID = manager.user_id, Username = manager.username), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST
        pass

    def login(self, json):
        if json['username'] and json['password']:
            manager = ManagerDAO().get(json['username'])
            if manager and sha256_crypt.verify(json['password'], manager.password):
                access_token = create_access_token(identity=manager.username)
                return jsonify(access_token = access_token), OK
            else:
                return jsonify(Error = 'user not found'), NOT_FOUND 
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST

    def edit(self, userid, json):
        if json['username'] and json['email'] and json['full_name']:
            user = Manager(userid, json['username'], json['email'], 0, json['full_name'])
            manager = ManagerDAO().edit(user)
            return jsonify(Manager=manager.serialize()), OK
        else:
            return jsonify(Error='Unexpected attributes in post'), BAD_REQUEST

    def delete(self, userid):
        manager = ManagerDAO().delete(userid)
        return jsonify(Manager=manager.serialize()), OK

    def getAll(self):
        managers = ManagerDAO().getAll()
        return jsonify(Manager=[manager.serialize() for manager in managers]), OK

    def get(self, userid):
        manager = ManagerDAO().get(userid)
        return jsonify(Manager=[manager.serialize()]), OK
