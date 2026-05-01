from fastapi import FastAPI
from services import suspect_logs
from fastapi import Body

app = FastAPI()

@app.get("/")
def log():
    return {"status": "API online"}
    
@app.post("/analise")
def take_log(dados: list = Body(...)):
    return suspect_logs(dados)
    