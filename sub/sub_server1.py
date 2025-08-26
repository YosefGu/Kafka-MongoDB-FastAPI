from fastapi import FastAPI
import os
from kafka_conn import KafkaConn
from mongodb_client import MongodbClient

app = FastAPI()

consumer = None
mongodb_client = None

@app.on_event("startup")
def startup_event():
    global consumer, mongodb_client
    consumer = KafkaConn(os.getenv('TOPIC'))
    mongodb_client = MongodbClient()



@app.get('/')
def home():
    return {"Active" : "Server is running"}

@app.get('/pull-data')
def pull_data():
    try:
        events = consumer.get_consumer_event()
        messages = []
        for message in events:
            messages.append(message.value)
        if not messages:
            return {"responce" : "No data in kafka topic."}
        
        mongodb_client.save_data(os.getenv('TOPIC'), messages)
        return {"responce" : "pulling and saving data went seccessfully.", "messages" : messages}
    except Exception as e:
        return {"Message" : "Error geting data from kafka", "Error" : str(e)}

@app.get('/get-data')
def get_data():
    try:
        cursor = mongodb_client.get_all_data(os.getenv('TOPIC'))
        list_result = []
        for doc in cursor:
           list_result.append(doc)
        return {"responce" : f"get data from {os.getenv('TOPIC')} collection went seccessfully.", "data" : list_result}
    except Exception as e:
        return {"Message" : "error geting data from mongodb.", "Error": str(e) }

        