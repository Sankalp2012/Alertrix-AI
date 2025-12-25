from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.pipeline import run_alert_pipeline

router = APIRouter(prefix="/api")

class EvaluateRequest(BaseModel):
    alert_text: str

class EvaluateResponse(BaseModel):
    triggered: bool
    confidence: float
    reason: str
    assumptions: list[str]

@router.post("/evaluate", response_model=EvaluateResponse)
async def evaluate_alert(req: EvaluateRequest):
    try:
        result = await run_alert_pipeline(req.alert_text)

        return EvaluateResponse(
            triggered=result.get("triggered", False),
            confidence=result.get("confidence", 0.0),
            reason=result.get("reason", ""),
            assumptions=result.get("assumptions", []),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
