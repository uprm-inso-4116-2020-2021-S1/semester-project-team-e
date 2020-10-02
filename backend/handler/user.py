from flask import jsonify
from handler.utils import OK, BAD_REQUEST, CREATED
from passlib.hash import sha256_crypt
from dao.user import UserDAO

class User:
    def register(self, json):
        if json['username'] and json['email'] and json['password']:
            if not UserDAO.get(json['username']):
                json['password'] = sha256_crypt.hash(json['password']) 
                user = UserDAO.add(json)
                return jsonify(isAuth = True, UserID = user[0], Username = user[1]), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST
        pass

    def login(self, json):
        if json['username'] and json['password']:
            user = UserDAO().get(json['username'])
            if sha256_crypt.verify(json['password'], user[3]):
                return jsonify(IsAuth = True, UserID = user[0], Username = user[1]), OK
            else:
                return jsonify(IsAuth = False), OK
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST
