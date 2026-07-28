import time
from threading import Lock

class AssistantState:
    def __init__(self):
        self.lock = Lock()

        # -------------------------
        # Original Assistant Status
        # -------------------------
        self.active = False
        self.status = "INACTIVE"
        self.last_gesture = ""
        self.last_command = ""
        self.pending_command = ""
        self.last_response = ""
        self.last_tool = ""
        self.current_frame = None
        self.ocr_capture = None
        self.ocr_scan = False
        self.ocr_duration = 3
        self.ocr_scan_countdown = 0
        self.current_document = ""
        self.pdfs = []
        self.conversation_history = []
        self.pending_action = ""
        self.pending_value = ""
        self.waiting_for_value = False

        # -------------------------
        # Added/Updated Variables
        # -------------------------
        self.last_uploaded_pdf = ""

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
    # GESTURE / COMMAND / TOOL / RESPONSE
    # ======================================================

    def set_gesture(self, gesture):
        with self.lock:
            self.last_gesture = gesture

    def set_command(self, command):
        with self.lock:
            self.last_command = command

    def set_pending_command(self, command):
        with self.lock:
            self.pending_command = command

    def get_pending_command(self):
        with self.lock:
            return self.pending_command

    def clear_pending_command(self):
        with self.lock:
            self.pending_command = ""

    def set_tool(self, tool):
        with self.lock:
            self.last_tool = tool

    def set_response(self, response):
        with self.lock:
            self.last_response = response

    def get_last_response(self):
        with self.lock:
            return self.last_response

    # Added setter for PDF
    def set_uploaded_pdf(self, filename):
        with self.lock:
            self.last_uploaded_pdf = filename

    # ======================================================
    # CAMERA / VISION / OCR (Kept original logic)
    # ======================================================

    def set_current_frame(self, frame):
        with self.lock:
            self.current_frame = frame.copy()

    def get_current_frame(self):
        with self.lock:
            return self.current_frame.copy() if self.current_frame is not None else None

    def set_ocr_capture(self, frame):
        with self.lock:
            self.ocr_capture = frame.copy()

    def get_ocr_capture(self):
        with self.lock:
            return self.ocr_capture

    def clear_ocr_capture(self):
        with self.lock:
            self.ocr_capture = None

    def start_ocr_scan(self, duration=3):
        with self.lock:
            self.ocr_scan = True
            self.ocr_duration = duration

    def stop_ocr_scan(self):
        with self.lock:
            self.ocr_scan = False
            self.ocr_duration = 0
            self.ocr_scan_countdown = 0
            if hasattr(self, "_ocr_start_time"):
                del self._ocr_start_time

    def is_ocr_scan_active(self):
        with self.lock:
            return self.ocr_scan

    def set_ocr_countdown(self, value):
        with self.lock:
            self.ocr_scan_countdown = value

    def get_ocr_countdown(self):
        with self.lock:
            return self.ocr_scan_countdown

    def update_ocr_countdown(self):
        with self.lock:
            if not self.ocr_scan:
                return 0
            if not hasattr(self, "_ocr_start_time"):
                self._ocr_start_time = time.time()
            elapsed = time.time() - self._ocr_start_time
            remaining = max(0, int(self.ocr_duration - elapsed + 0.999))
            self.ocr_scan_countdown = remaining
            if remaining <= 0:
                self.ocr_scan = False
            return remaining

    # ======================================================
    # CURRENT DOCUMENT & PDFs (Kept original logic)
    # ======================================================

    def set_current_document(self, text):
        with self.lock:
            self.current_document = text

    def get_current_document(self):
        with self.lock:
            return self.current_document

    def clear_current_document(self):
        with self.lock:
            self.current_document = ""

    def add_pdf(self, filename, text):
        with self.lock:
            self.pdfs.append({"filename": filename, "text": text})

    def get_all_pdfs(self):
        with self.lock:
            return self.pdfs.copy()

    def get_all_pdf_text(self):
        with self.lock:
            if not self.pdfs: return ""
            combined = ""
            for pdf in self.pdfs:
                combined += f"\n\n========== {pdf['filename']} ==========\n\n"
                combined += pdf["text"]
            return combined

    def remove_pdf(self, filename):
        with self.lock:
            self.pdfs = [p for p in self.pdfs if p["filename"] != filename]

    def clear_pdfs(self):
        with self.lock:
            self.pdfs.clear()

    # ======================================================
    # CONVERSATION MEMORY (Updated to limit 20)
    # ======================================================

    def add_conversation(self, user, assistant):
        with self.lock:
            self.conversation_history.append({"user": user, "assistant": assistant})
            if len(self.conversation_history) > 20:
                self.conversation_history.pop(0)

    def get_history(self):
        with self.lock:
            return self.conversation_history.copy()

    def build_history(self):
        with self.lock:
            history = ""
            for chat in self.conversation_history:
                history += f"User: {chat['user']}\nAssistant: {chat['assistant']}\n\n"
            return history

    def clear_history(self):
        with self.lock:
            self.conversation_history.clear()

    # ======================================================
    # PENDING ACTION
    # ======================================================

    def start_pending_action(self, action, value):
        with self.lock:
            self.pending_action = action
            self.pending_value = value
            self.waiting_for_value = True

    def has_pending_action(self):
        with self.lock:
            return self.waiting_for_value

    def get_pending_action(self):
        with self.lock:
            return (self.pending_action, self.pending_value)

    def clear_pending_action(self):
        with self.lock:
            self.pending_action = ""
            self.pending_value = ""
            self.waiting_for_value = False

    # ======================================================
    # FRONTEND
    # ======================================================

    def get_state(self):
        with self.lock:
            return {
                "active": self.active,
                "status": self.status,
                "last_gesture": self.last_gesture,
                "last_command": self.last_command,
                "last_tool": self.last_tool,
                "last_response": self.last_response,
                "last_uploaded_pdf": self.last_uploaded_pdf,
                "conversation": self.conversation_history.copy(),
            }

assistant_state = AssistantState()