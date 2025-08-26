from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

from fetching import Fetching
from connector import Connector


load_dotenv()


app = FastAPI()

connector = Connector()

fetching = Fetching()
fetching.fetch_data()


@app.get('/')
def home():
    return {"Active" : "Server is running"}

@app.get('/publish-data')
def publish_data():
    data = fetching.get_20_messages()
    for i in range(10):
        connector.publish_message(os.getenv('TOPIC_1'), data['interesting'].pop(0))
        connector.publish_message(os.getenv('TOPIC_2'), data['not_interesting'].pop(0))
    return {"responce" : "Publishing went seccessfully."}

if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8001)
    except Exception as e:
        print("Error running server")
        