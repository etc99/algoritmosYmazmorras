from pymongo import MongoClient

MONGO_URL = "mongodb://mongodb:27017/"
MONGO_DB = "mazmorras"


class DataBase:
    db = MongoClient = None

    def connect(self):
        self.db = MongoClient(MONGO_DB)

    
    def  disconnect(self):
         self.db.client.close()

    def get_db(self):
        return self.db
