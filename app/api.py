from fastapi import FastAPI
from pydantic import BaseModel
from app.pipeline import run_alert_pipeline

app = FastAPI()

class AlertRequest(BaseModel):
    alert_text: str

class AlertResponse(BaseModel):
    triggered: bool
    confidence: int
    reason: str
    assumptions: list[str]

@app.post("/evaluate", response_model=AlertResponse)
async def evaluate_alert(req: AlertRequest):
    result = await run_alert_pipeline(req.alert_text)

    return {
        "triggered": result["triggered"],
        "confidence": result["confidence"],
        "reason": result["reason"],
        "assumptions": result["assumptions"],
    }
