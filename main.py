from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def log():
    return {"status": "API online"}
    

    
    


