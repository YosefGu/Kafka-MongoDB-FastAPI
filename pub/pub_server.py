from fastapi import FastAPI
from fetching import Fetching
from connector import Connector

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
        connector.publish_message('interesting', data['interesting'].pop(0))
        connector.publish_message('not_interesting', data['not_interesting'].pop(0))
    return {"responce" : "Publishing went seccessfully."}


        