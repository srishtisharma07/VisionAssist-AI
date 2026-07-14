from threading import Thread

from app.agents.orchestrator import agent
from app.services.assistant_state import assistant_state
from app.services.assistant_status import AssistantStatus
from app.speech.speech_to_text import speech_to_text
from app.speech.text_to_speech import text_to_speech


class ListenerService:

    def __init__(self):

        self.is_listening = False

    def start(self):

        if self.is_listening:

            print("Already listening...")

            return

        if not assistant_state.active:

            print("Assistant is inactive.")

            return

        self.is_listening = True

        assistant_state.set_status(
            AssistantStatus.LISTENING
        )

        

        Thread(
            target=self.listen_loop,
            daemon=True,
        ).start()

    def listen_loop(self):

        try:

            print("\n==============================")
            print("Listening...")
            print("==============================\n")

            command = speech_to_text.listen()

            if not command:

                assistant_state.set_status(
                    AssistantStatus.ACTIVATED
                )

                return

            assistant_state.set_command(command)

            result = agent.execute(command)

            response = result["response"]

            assistant_state.set_response(response)

            assistant_state.set_status(
                AssistantStatus.SPEAKING
            )

            text_to_speech.speak(response)

            assistant_state.set_status(
                AssistantStatus.ACTIVATED
            )

        except Exception as e:

            assistant_state.set_status(
                AssistantStatus.ERROR
            )

            print("\nListener Error:")
            print(e)

        finally:

            self.is_listening = False


listener_service = ListenerService()