from fastapi import FastAPI
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
import requests
import os

load_dotenv()

#consumir api    
def fetch_api():
    payload = {"message": "user-signed-in"}
    res = requests.post(os.getenv("API"),json=payload)
    return res.text

#poner intervalo
@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_api,"interval",seconds=int(os.getenv("INTERVAL")))
    scheduler.start()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def test():
    return "Ok"