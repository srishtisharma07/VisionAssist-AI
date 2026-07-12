from app.agents.orchestrator import agent
from app.services.assistant_state import assistant_state


class GestureController:

    def __init__(self):

        self.gesture_commands = {
            "THUMBS UP": "Summarize the uploaded PDF.",
            "VICTORY": "Translate the previous response into Hindi.",
            "FIST": "Explain the previous response in simple language.",
            "OPEN PALM": "Save this response as PDF.",
            "THUMBS DOWN": "Save this response as TXT.",
        }

    def execute(self, gesture: str):

        if gesture not in self.gesture_commands:
            return

        command = self.gesture_commands[gesture]

        print("\n" + "=" * 60)
        print(f"GESTURE DETECTED : {gesture}")
        print(f"EXECUTING COMMAND: {command}")
        print("=" * 60)

        result = agent.execute(command)

        assistant_state.set_response(result["response"])

        print("\n" + "=" * 60)
        print("AGENT RESPONSE")
        print("=" * 60)
        print(result["response"])
        print("=" * 60 + "\n")


gesture_controller = GestureController()