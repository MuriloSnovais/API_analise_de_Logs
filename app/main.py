from fastapi import FastAPI
from app.services import suspect_logs
from pydantic import BaseModel

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
