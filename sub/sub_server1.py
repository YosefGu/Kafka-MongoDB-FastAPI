from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os
from kafka_conn import KafkaConn
from mongodb_client import MongodbClient


load_dotenv()

consumer = KafkaConn(os.getenv('TOPIC_1'))
mongodb_client = MongodbClient()

app = FastAPI()

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
        
        mongodb_client.save_data(os.getenv('TOPIC_1'), messages)
        return {"responce" : "pulling and saving data went seccessfully.", "messages" : messages}
    except Exception as e:
        print(e)
        return {"Message" : "Error geting data from kafka", "Error" : e}

@app.get('/get-data')
def get_data():
    try:
        cursor = mongodb_client.get_all_data(os.getenv('TOPIC_1'))
        list_result = []
        for doc in cursor:
           list_result.append(doc)
        return {"responce" : f"get data from {os.getenv('TOPIC_1')} collection went seccessfully.", "data" : list_result}
    except Exception as e:
        return {"Message" : "error geting data from mongodb.", "Error": e }


if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8002)
    except Exception as e:
        print("Error running server")
        