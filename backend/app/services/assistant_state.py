from threading import Lock


class AssistantState:
    def __init__(self):
        self.lock = Lock()

        self.active = False
        self.last_gesture = ""
        self.last_command = ""
        self.last_response = ""

    def activate(self):
        with self.lock:
            self.active = True

    def deactivate(self):
        with self.lock:
            self.active = False

    def set_gesture(self, gesture):
        with self.lock:
            self.last_gesture = gesture

    def set_command(self, command):
        with self.lock:
            self.last_command = command

    def set_response(self, response):
        with self.lock:
            self.last_response = response

    def get_state(self):
        with self.lock:
            return {
                "active": self.active,
                "last_gesture": self.last_gesture,
                "last_command": self.last_command,
                "last_response": self.last_response,
            }


assistant_state = AssistantState()