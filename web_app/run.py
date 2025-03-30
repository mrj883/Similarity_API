from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_restful import Api, Resource
import spacy
import os
import logging


app = Flask(__name__)
api = Api(app)


#Mongo DB setup
client = MongoClient("mongodb://27017")

# paraments for the app
# username
# password
# Admin_password
# tokens
# text_1 : text_2




def check_format(Resource, input_data):
    #Validaation for Register input
    if Resource == "Register" and "password" in input_data and "username":
        return True
            
    #validation Resource2
    #validation R2



    return False   


class Register(Resource):
    def post(self):
        pjson  = request.get_json()
        if not check_format("Register", pjson): 
            jret = {
                "Status_code" : 200,
                "Message": "insufficient parameter"
            }
            return jsonify(jret)
        pass
        
class DetectSimilarity(Resource):
    def post(self):
        pjson = request.get_json()
        if check_format()




        
        






@app.route("/")
def Welcome():

    return "welcome to the home page"




if __name__=="__main__":
    app.run()

