# ==========================================
# REQUEST MODELS
# ==========================================

from pydantic import BaseModel

class AdaptRequest(BaseModel):

    user_id: str

    confidence: float | None = None

    correctness: int