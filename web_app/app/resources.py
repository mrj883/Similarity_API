from flask_restful import Resource
import bcrypt
from .authentication import checkExists, authenticate
from flask import request, jsonify
from .db_handler import add_user
class RegisterUser(Resource):
    def post(self):
        jreq = request.get_json()
        status_code =  checkExists(jreq) 
        if status_code == 301:
            jret = {
             "Status code" : "301",
             "Message" : "Username Already exists"   
            }
            return jsonify(jret)
        elif status_code == 305:
            jret ={
                "Status code" : 305,
                "Message": "the parameters are insufficient to make the request"
            }
            return jsonify(jret)
        
        successful, Message = add_user(jreq)
        
        
        if successful :
            status_code = 200
            Message = "Registration was successfull"
            jret = {
                "Status Code": status_code,
                "Message" : Message
            }
            return jsonify(jret)
        else:
            status_code = 303
            jret = {
                "Status Code": status_code,
                "Message" : Message
            }
            return jsonify(jret)
            
    



