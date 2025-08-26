from pymongo import MongoClient
import os
from datetime import datetime

class MongodbClient():

    def __init__(self):
        self.user = os.getenv('MONGO_USER')
        self.password = os.getenv('MONGO_PASSWORD')
        self.host = os.getenv('MONGO_HOST')
        self.port = os.getenv('MONGO_PORT', '27017')

        self.client = MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/')
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
    

