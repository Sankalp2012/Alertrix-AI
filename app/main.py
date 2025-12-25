from fastapi import FastAPI
from app.api import router  # assuming you moved endpoints to api.py

app = FastAPI(title="Alertrix AI Engine")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "alertrix-ai",
    }

app.include_router(router)
