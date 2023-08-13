import pymongo
import os
from dotenv import load_dotenv  #, dotenv_values

class DbHandler:
    """Initialize with mongodb connection string and the name of the database name to use"""
    def __init__(self, connection_str, db_name):
        #LOad .env variables
        load_dotenv()
        self.connection_str = connection_str
        self.cluster= pymongo.MongoClient(connection_str)
        self.db = self.cluster[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def insert_one(self, collection_name, document):
        collection = self.get_collection(collection_name)
        collection.insert_one(document)


connection_str = os.getenv("MONGO_DB_CONNECTION_STR")
db_handler = DbHandler(connection_str, "test")
users_collections = db_handler.get_collection("users")
documents = users_collections.find({})

print(documents)




#collection_users.insert_one({"name": "Macario Lopez", "Address": "unknown"})
#users = collection_users.find({})

