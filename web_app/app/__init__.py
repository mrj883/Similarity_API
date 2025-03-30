from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient





def create_app():
    app = Flask(__name__)
    api = Api(app)
    