import pymongo
from configparser import ConfigParser
from pymongo import MongoClient

config = ConfigParser()
config.read("config.ini")

client = MongoClient(config['DATABASE']['CONNECTIONSTRING'])
db = client[config['DATABASE']['DB']]
users_collection = db[config['DATABASE']['COLLECTIONUSERS']]
queries_collection = db[config['DATABASE']['COLLECTIONQUERIES']]

def create_user(new_name,new_email,new_date, new_password) -> int:
    if users_collection.find_one({"_id": new_email}):
        return 0
    user = {"_id": new_email,"name": new_name,"DOB":new_date, "password": new_password}
    users_collection.insert_one(user)
    return 1

def authenticate_user(email, password):
    user = users_collection.find_one({"_id": email, "password": password})
    if user:
        return True
    return False

def get_user_queries(email):
    user_queries = queries_collection.find_one({"_id": email})
    if user_queries:
        return {k.replace("__dot__", "."): v for k, v in user_queries.items() if k != '_id'}
    return {}

def update_user_queries(username, queries):
    sanitized_queries = {k.replace(".", "__dot__"): v for k, v in queries.items()}
    queries_collection.update_one({"_id": username}, {"$set": sanitized_queries}, upsert=True)

def update_user(new_email,new_date, new_password) -> int:
        if not users_collection.find_one({"_id": new_email}):
             return 0
        elif not users_collection.find_one({"_id": new_email, "DOB":new_date}):
             return 1
        else:
             users_collection.update_one({"_id": new_email}, {"$set": {"password": new_password}})
             return 2

def getname(email):
    user = users_collection.find_one({"_id": email})
    return user['name']

def clear_chats(email):
     queries_collection.delete_one({"_id": email})

def delete_acc(email, password):
    if users_collection.find_one({"_id": email, "password": password}):
         users_collection.delete_one({"_id": email, "password": password})
         queries_collection.delete_one({"_id": email})
         return 1
    else:
         return 0