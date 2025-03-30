from flask_restful import Resource
import bcrypt
from .authentication import checkExists, authenticate
from flask import request

class RegisterUser(Resource):
    def post(self):
        jreq = request.get_json()

