from fastapi import FastAPI
from services import suspect_logs

app = FastAPI()

@app.get("/")
def log():
    return {"status": "API online"}
    
@app.post("/analise")
def take_log():
    return suspect_logs()
    
    

    
    


