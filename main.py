from os import environ

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi import APIRouter, Body, Depends
from v1.modules.utils import BaseResponse
from v1.modules.translate import translate
from v1.modules.send_message import SendMessage
import json
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Chat(BaseModel):
    id: int
    first_name: str
    last_name: str
    type: str

class Message(BaseModel):
    message_id: float
    text: str
    chat: Chat

class TelegramMessage(BaseModel):
    update_id: int
    message: Message

# from v1.app import routes 

app = FastAPI()

# app.include_router(routes)

@app.post("/")
async def list_foo(payload: TelegramMessage):
    send_message = SendMessage()
    payload = json.loads(payload.json())
    message = payload['message']['text']
    translate_response = translate(message)
    send_message= send_message.tel_send_message(payload['message']['chat']['id'],translate_response)
    
    return BaseResponse(message="Foo list", data='foo_list')
