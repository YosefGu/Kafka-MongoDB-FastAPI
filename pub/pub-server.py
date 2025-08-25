from fastapi import FastAPI
import uvicorn
from fetching import Fetching
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

fetching = Fetching()
fetching.fetch_data()


@app.get('/')
def home():
    return {"Active" : "Server is running"}

@app.get('/get-data')
def get_data():
    return fetching.get_20_messages()


if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8001)
    except Exception as e:
        print("Error running server")
        