from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os
from kafka_conn import KafkaConn

load_dotenv()

consumer = KafkaConn(os.getenv('TOPIC_1'))

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
        return {"responce" : "pulling seccessfully.", "data" : messages}
    except Exception as e:
        print("Error pulling data.")
        print(e)

@app.get('/get-data')
def get_data():
   pass

if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8002)
    except Exception as e:
        print("Error running server")
        