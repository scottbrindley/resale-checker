from fastapi import FastAPI
from resale_checker import check_resales

app = FastAPI()

@app.get("/run")
def run():
    resale_events = check_resales()
    return {"status": "ok", "resale_events": resale_events}

@app.get("/test")
def test():
    return {"status": "ok", "message": "API called successfully"}
