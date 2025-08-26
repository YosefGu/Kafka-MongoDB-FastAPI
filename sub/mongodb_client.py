from pymongo import MongoClient
import os
from datetime import datetime

class MongodbClient():

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_CONN'))
        self.database = self.client['kafka-project']

    def save_data(self, collection, data):
        try: 
            col = self.database[collection]
            for doc in data:
                col.insert_one({"datatime" : datetime.now(), "message" : doc})
        except Exception as e:
            print("Error saveing data.")

    def get_all_data(self, collection):
        try:
            data = self.database[collection].find({}, {'_id' : 0})
            return data
        except Exception as e:
            print("Error geting data.")
    

