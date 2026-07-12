from threading import Thread

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agents.orchestrator import agent
from app.gestures.gesture_detector import GestureDetector
from app.routers.pdf_router import router as pdf_router
from app.routers.speech_router import router as speech_router
from app.services.assistant_state import assistant_state

app = FastAPI(
    title="VisionAssist AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():

    detector = GestureDetector()

    Thread(
        target=detector.start,
        daemon=True,
    ).start()


app.include_router(pdf_router)
app.include_router(speech_router)


@app.get("/")
def home():

    return {
        "message": "VisionAssist AI Backend Running"
    }


@app.get("/state")
def get_state():

    return assistant_state.get_state()


@app.get("/agent")
def run_agent(command: str):

    result = agent.execute(command)

    return result