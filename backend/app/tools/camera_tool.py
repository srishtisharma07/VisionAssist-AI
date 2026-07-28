from pathlib import Path
import cv2
import numpy as np
import time
import inspect

from app.services.assistant_state import assistant_state
from app.speech.text_to_speech import text_to_speech
from app.tools.ocr_tool import ocr_tool

# Debugging assistant_state.start_ocr_scan signature
print(f"Signature of assistant_state.start_ocr_scan: {inspect.signature(assistant_state.start_ocr_scan)}")


class CameraTool:

    def __init__(self):
        self.image_path = Path("uploads/ocr_image.jpg")
        self.image_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def calculate_sharpness(self, image):
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        return cv2.Laplacian(
            gray,
            cv2.CV_64F,
        ).var()

    def capture_text(self):
        # Clear previous capture
        assistant_state.clear_ocr_capture()

        # Start OCR scan
        assistant_state.start_ocr_scan(duration=3)

        print("\nWaiting for document scan...\n")

        # Wait until gesture detector captures the image
        while assistant_state.is_ocr_scan_active():
            time.sleep(0.1)

        # Get captured image
        frame = assistant_state.get_ocr_capture()
        
        # Save the captured scan for verification
        cv2.imwrite("captured_scan.jpg", frame)

        if frame is None:
            return "No document was captured."

        # Save for debugging
        cv2.imwrite(str(self.image_path), frame)

        try:
            text = ocr_tool.read_image(frame)

            if not text.strip():
                return "No readable text found."

            assistant_state.set_current_document(text)
            return text

        except Exception as e:
            print(f"OCR Error: {e}")
            return "Unable to read the document."

camera_tool = CameraTool()