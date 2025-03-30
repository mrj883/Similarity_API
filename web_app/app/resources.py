from flask_restful import Resource
import bcrypt

class RegisterResource(Resource):
    def post(self):