from db.mongodb import mongoDB
from config.config import config
from datetime import datetime
from bson.objectid import ObjectId
class MongoAccions(object):
    def aggregate(collection, pipeline):
        try:
            db = mongoDB.db[collection]
            agg = db.aggregate(pipeline)
            return list(agg)
        except ValueError as err:
            print(err)
            return None
    def deleteUser(id):
        try:
            filter = {'_id': ObjectId(id)}
            newValues = {"$set":{
                'active': False
            }}
            db = mongoDB.db['users']
            result= db.update_one(filter, newValues)
            if result.matched_count > 0:
                return True
            else:
                return False
        except ValueError as err:
            print(err)
            return False
    def modifyUser(name, lastName, id):
        try:
            filter = {'_id': ObjectId(id)}
            newValues = {"$set":{
                'name': name,
                'last_name': lastName
            }}
            db = mongoDB.db['users']
            result= db.update_one(filter, newValues)
            if result.matched_count > 0:
                return True
            else:
                return False
        except ValueError as err:
            print(err)
            return False
    def createUser(name, lastName):
        try:
            dateEntry = datetime.utcnow()
            uniqueId = MongoAccions.getUniqueId()
            if not uniqueId:
                return False 
            userData = {
                'name': name,
                'last_name': lastName,
                'uniqueId': uniqueId,
                'dateEntry': dateEntry,
                'active': True
            }
            db = mongoDB.db['users']
            insert = db.insert_one(userData)
            insertId = insert.inserted_id
            if not insertId:
                return False
            else:
                return True
        except ValueError as err:
            print(err)
            return False
    @staticmethod
    def getUniqueId():
        try:
            db = mongoDB.db['users']
            agg = list(db.find().sort("dateEntry", -1).limit(1))
            print(agg)
            if not agg:
                return 1
            else:
                lastUser = list(agg)[0]
                return int(lastUser['uniqueId']) + 1
        except ValueError as err:
            print(err)
            return False