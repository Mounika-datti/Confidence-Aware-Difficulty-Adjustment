# ==========================================
# MAIN FASTAPI SERVER
# ==========================================
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header

from models import AdaptRequest

from validator import validate_input

from auth import authenticate

from engine import AdaptiveEngine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)
engine = AdaptiveEngine()

# ------------------------------------------
# Root Endpoint
# ------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Adaptive Difficulty API Running"
    }

# ------------------------------------------
# Adapt Endpoint
# ------------------------------------------

@app.post("/adapt")
def adapt(
    request: AdaptRequest,
    x_api_key: str = Header(...)
):

    # Authentication Layer
    if not authenticate(x_api_key):

        return {
            "error": "Unauthorized"
        }

    # Validation Layer
    confidence, correctness = validate_input(

        request.confidence,

        request.correctness
    )

    # Adaptive Decision Engine
    result = engine.adapt(

        user_id=request.user_id,

        confidence=confidence,

        correctness=correctness
    )

    # Difficulty Response
    return result