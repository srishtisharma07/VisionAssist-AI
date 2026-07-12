from threading import Lock


class AssistantState:

    def __init__(self):

        self.lock = Lock()

        # -------------------------
        # Assistant Status
        # -------------------------
        self.active = False
        self.status = "INACTIVE"

        # -------------------------
        # Gesture
        # -------------------------
        self.last_gesture = ""

        # -------------------------
        # Voice
        # -------------------------
        self.last_command = ""
        self.last_response = ""

        # -------------------------
        # Tool
        # -------------------------
        self.last_tool = ""

        # -------------------------
        # Multiple PDFs
        # -------------------------
        self.pdfs = []

        # -------------------------
        # Conversation Memory
        # -------------------------
        self.conversation_history = []

    # ======================================================
    # STATUS
    # ======================================================

    def activate(self):

        with self.lock:

            self.active = True
            self.status = "ACTIVE"

    def deactivate(self):

        with self.lock:

            self.active = False
            self.status = "INACTIVE"

    def set_status(self, status):

        with self.lock:

            self.status = status

    def get_status(self):

        with self.lock:

            return self.status

    # ======================================================
    # GESTURE
    # ======================================================

    def set_gesture(self, gesture):

        with self.lock:

            self.last_gesture = gesture

    # ======================================================
    # COMMAND
    # ======================================================

    def set_command(self, command):

        with self.lock:

            self.last_command = command

    # ======================================================
    # RESPONSE
    # ======================================================

    def set_response(self, response):

        with self.lock:

            self.last_response = response

    def get_last_response(self):

        with self.lock:

            return self.last_response

    # ======================================================
    # TOOL
    # ======================================================

    def set_tool(self, tool):

        with self.lock:

            self.last_tool = tool

    # ======================================================
    # MULTIPLE PDF SUPPORT
    # ======================================================

    def add_pdf(self, filename, text):

        with self.lock:

            self.pdfs.append(
                {
                    "filename": filename,
                    "text": text,
                }
            )

    def get_all_pdfs(self):

        with self.lock:

            return self.pdfs.copy()

    def get_all_pdf_text(self):

        with self.lock:

            if not self.pdfs:
                return ""

            combined = ""

            for pdf in self.pdfs:

                combined += (
                    f"\n\n========== {pdf['filename']} ==========\n\n"
                )

                combined += pdf["text"]

            return combined

    def remove_pdf(self, filename):

        with self.lock:

            self.pdfs = [

                pdf

                for pdf in self.pdfs

                if pdf["filename"] != filename

            ]

    def clear_pdfs(self):

        with self.lock:

            self.pdfs.clear()

    # ======================================================
    # MEMORY
    # ======================================================

    def add_conversation(self, user, assistant):

        with self.lock:

            self.conversation_history.append(

                {
                    "user": user,
                    "assistant": assistant,
                }

            )

            if len(self.conversation_history) > 15:

                self.conversation_history.pop(0)

    def get_history(self):

        with self.lock:

            return self.conversation_history.copy()

    def build_history(self):

        with self.lock:

            history = ""

            for chat in self.conversation_history:

                history += f"User: {chat['user']}\n"

                history += f"Assistant: {chat['assistant']}\n\n"

            return history

    def clear_history(self):

        with self.lock:

            self.conversation_history.clear()

    # ======================================================
    # FRONTEND
    # ======================================================

    def get_state(self):

        with self.lock:

            return {

                "active": self.active,

                "status": self.status,

                "gesture": self.last_gesture,

                "command": self.last_command,

                "response": self.last_response,

                "tool": self.last_tool,

                "uploaded_pdfs": [

                    pdf["filename"]

                    for pdf in self.pdfs

                ],

                "conversation_history": self.conversation_history,

            }


assistant_state = AssistantState()