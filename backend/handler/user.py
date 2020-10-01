from flask import jsonify
from handler.utils import OK, BAD_REQUEST
from passlib.hash import sha256_crypt
from dao.user import UserDAO

class User:
    def register(self, json):
        pass

    def login(self, json):
        if json['username'] and json['password']:
            user = UserDAO().get(json['username'])
            if sha256_crypt.verify(json['password'], user[3]):
                return jsonify(IsAuth = True, UserID = user[0]), OK
            else:
                return jsonify(IsAuth = False), OK
        else:
            return jsonify(Error = 'Unexpected attributes in post'), BAD_REQUEST
