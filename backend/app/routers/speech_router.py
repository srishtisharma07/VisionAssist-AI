from fastapi import APIRouter

from app.agents.orchestrator import agent
from app.services.assistant_state import assistant_state
from app.speech import speech_to_text, text_to_speech

router = APIRouter(
    prefix="/speech",
    tags=["Speech"],
)


@router.get("/listen")
def listen():

    command = speech_to_text.listen()

    if not command:
        return {
            "message": "No speech detected."
        }

    assistant_state.set_command(command)

    result = agent.execute(command)

    response = result["response"]

    assistant_state.set_response(response)

    text_to_speech.speak(response)

    return {
        "command": command,
        "response": response,
    }