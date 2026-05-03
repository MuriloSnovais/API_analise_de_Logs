from fastapi import FastAPI
from services import suspect_logs
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class logBase(BaseModel):
    ip: str
    login: str

@app.get("/")
def log():
    return {"status": "API online"}
    
@app.post("/analise")
def take_log(dados: list[logBase]):
    return suspect_logs(dados)
    