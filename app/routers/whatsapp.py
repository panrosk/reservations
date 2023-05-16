from fastapi import APIRouter, FastAPI
import os
from services.langchain.chain import get_chain
from models.whatsapp import Whastapp
router = APIRouter(
    prefix="/whatsapp",
)



@router.post("/")
async def send_whatsapp_message(message:Whastapp):
    chain = get_chain(KEY=os.getenv("OPEN_API_KEY"))
    resultado = chain.predict(human_input=message.text)
    print(chain.memory)
    return { "message":resultado}

@router.get("/")
async def get_whatsapp_message():
    return {"message": "hola"}


