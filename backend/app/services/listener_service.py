from threading import Thread

from app.services.assistant_state import assistant_state
from app.services.assistant_status import AssistantStatus
from app.speech.speech_to_text import speech_to_text
from app.speech.text_to_speech import text_to_speech
from app.agents.correction_agent import correction_agent


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

            # =====================================================
            # CONTINUE PENDING FILE CONVERSATION
            # =====================================================
            if assistant_state.has_pending_action():
                action, expected = assistant_state.get_pending_action()
                assistant_state.clear_pending_action()

                if action == "create_folder":
                    command = f"create folder {command}"
                elif action == "delete_folder":
                    command = f"delete folder {command}"
                elif action == "create_file":
                    command = f"create file {command}"
                elif action == "delete_file":
                    command = f"delete file {command}"

                print(f"Pending action: {action}")
                print(f"Final command: {command}")
                
                print("\n==============================")
                print("FULL COMMAND")
                print("==============================")
                print(command)
                print("==============================")

            # Correct only file/system commands
            if command:
                correction_keywords = [
                    "create",
                    "delete",
                    "rename",
                    "move",
                    "copy",
                    "open",
                    "folder",
                    "file",
                    "downloads",
                    "desktop",
                    "documents",
                    "pictures",
                ]

                if any(word in command.lower() for word in correction_keywords):
                    command = correction_agent.correct(command)

            if not command:
                assistant_state.set_status(
                    AssistantStatus.ACTIVATED
                )
                return

            lower = command.lower().strip()
            
            # ----------------------------------------------------
            # CREATE FOLDER
            # ----------------------------------------------------
            if lower == "create folder":
                assistant_state.start_pending_action("create_folder", "folder_name")
                assistant_state.set_status(AssistantStatus.ACTIVATED)
                self.is_listening = False
                text_to_speech.speak(
                    "What should be the folder name?",
                    on_complete=self.start,
                )
                return

            # ----------------------------------------------------
            # DELETE FOLDER
            # ----------------------------------------------------
            if lower == "delete folder":
                assistant_state.start_pending_action("delete_folder", "folder_name")
                assistant_state.set_status(AssistantStatus.ACTIVATED)
                self.is_listening = False
                text_to_speech.speak(
                    "Which folder should I delete?",
                    on_complete=self.start,
                )
                return

            # ----------------------------------------------------
            # CREATE FILE
            # ----------------------------------------------------
            if lower == "create file":
                assistant_state.start_pending_action("create_file", "file_name")
                assistant_state.set_status(AssistantStatus.ACTIVATED)
                self.is_listening = False
                text_to_speech.speak(
                    "What should be the file name?",
                    on_complete=self.start,
                )
                return

            # ----------------------------------------------------
            # DELETE FILE
            # ----------------------------------------------------
            if lower == "delete file":
                assistant_state.start_pending_action("delete_file", "file_name")
                assistant_state.set_status(AssistantStatus.ACTIVATED)
                self.is_listening = False
                text_to_speech.speak(
                    "Which file should I delete?",
                    on_complete=self.start,
                )
                return

            assistant_state.set_command(command)
            assistant_state.set_pending_command(command)
            assistant_state.set_status(AssistantStatus.CONFIRMING)

            print("\n==============================")
            print("VOICE COMMAND")
            print("==============================")
            print(command)
            print("==============================")
            print("Thumbs Up   -> Execute")
            print("Thumbs Down -> Speak Again")
            print("==============================")

            text_to_speech.speak(
                "I heard. " + command +
                ". Show thumbs up to confirm or thumbs down to speak again."
            )

        except Exception as e:
            assistant_state.set_status(AssistantStatus.ERROR)
            print("\nListener Error:")
            print(e)

        finally:
            self.is_listening = False


listener_service = ListenerService()