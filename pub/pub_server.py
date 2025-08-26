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
def get_data():
    data = fetching.get_20_messages()
    connector.publish_message(os.getenv('TOPIC_1'), data['interesting'])
    connector.publish_message(os.getenv('TOPIC_2'), data['not_interesting'])
    return {"responce" : "Publishing went seccessfully."}

if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8001)
    except Exception as e:
        print("Error running server")
        