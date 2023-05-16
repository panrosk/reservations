from fastapi import FastAPI
from routers import whatsapp
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

app.include_router(whatsapp.router)

@app.get("/")
def read_root():

    return {"Hello": "World"}