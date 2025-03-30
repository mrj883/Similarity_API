from pymongo import MongoClient

client = MongoClient("mongodb://27017")
db = client.Similarity_DB
collection = db["user_details"]

def get_db():
    return db


def get_user_collection():
    return collection