from unicodedata import name
import pymongo
from pymongo import MongoClient

mongo_host = "localhost"
mongo_port = 27017
mongo_dbname = "spla-database"
mongo_collection = "users-collection"

class Mongo_Command:
    def __init__(self) -> None:
        self.client = MongoClient(mongo_host,mongo_port)
        self.db = self.client[mongo_dbname]
        self.collection = self.db[mongo_collection]

    def test_post_one(self):
        self.collection.insert_one({"testkey":"testvalue"})

if __name__ == "__main__":
    Mtest = Mongo_Command()
    Mtest.test_post_one()
    # Mtest.test_post_one()