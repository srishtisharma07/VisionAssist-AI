import time
import threading
import cv2
import mediapipe as mp

from app.services.assistant_state import assistant_state
from app.services.assistant_status import AssistantStatus
from app.services.listener_service import listener_service
from app.services.camera_service import camera_service
from app.agents.orchestrator import agent
from app.speech.text_to_speech import text_to_speech

class GestureDetector:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
        )

        # Stable gesture detection
        self.current_gesture = ""
        self.gesture_start_time = 0
        self.hold_time = 0.8
        self.last_executed = ""

    # =====================================================

    def get_finger_states(self, landmarks):
        fingers = []

        # Thumb folded/open
        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # Remaining fingers
        for tip in [8, 12, 16, 20]:
            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    # =====================================================

    def thumb_direction(self, landmarks):
        thumb_tip = landmarks[4]
        wrist = landmarks[0]

        if thumb_tip.y < wrist.y:
            return "UP"
        if thumb_tip.y > wrist.y:
            return "DOWN"
        return "NONE"

    # =====================================================

    def recognize_gesture(self, landmarks):
        fingers = self.get_finger_states(landmarks)
        thumb = self.thumb_direction(landmarks)

        if fingers == [1, 1, 1, 1, 1]:
            return "OPEN PALM"
        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"
        if fingers == [0, 1, 0, 0, 0]:
            return "INDEX"
        if fingers == [0, 1, 1, 0, 0]:
            return "VICTORY"

        # Better thumbs
        if fingers[1:] == [0, 0, 0, 0]:
            if thumb == "UP":
                return "THUMBS UP"
            if thumb == "DOWN":
                return "THUMBS DOWN"

        return ""

    # =====================================================

    def execute_command(self, command):
        assistant_state.set_status(AssistantStatus.THINKING)
        result = agent.execute(command)
        response = result["response"]
        text_to_speech.speak(response)
        assistant_state.set_status(AssistantStatus.ACTIVATED)

    # =====================================================

    def retry_command(self):
        text_to_speech.speak(
            "Okay. Please say the command again.",
            on_complete=listener_service.start,
        )

    # =====================================================

    def process_gesture(self, gesture):
        if not gesture:
            return

        assistant_state.set_gesture(gesture)
        print(f"\nDetected Gesture: {gesture}")

        # While confirming, ignore every gesture except 👍 👎 ✊
        if assistant_state.get_status() == AssistantStatus.CONFIRMING:
            if gesture not in ["THUMBS UP", "THUMBS DOWN", "FIST"]:
                return

        # OPEN PALM
        if gesture == "OPEN PALM":
            if assistant_state.active:
                return
            assistant_state.activate()
            print("\n==============================")
            print("Assistant Activated")
            print("==============================")
            return

        # FIST
        if gesture == "FIST":
            if not assistant_state.active:
                return
            text_to_speech.stop()
            assistant_state.deactivate()
            assistant_state.clear_pending_command()
            print("\n==============================")
            print("Assistant Deactivated")
            print("==============================")
            return

        # INDEX
        if gesture == "INDEX":
            if not assistant_state.active:
                return
            if assistant_state.get_status() == AssistantStatus.CONFIRMING:
                return
            listener_service.start()
            return

        # THUMBS UP
        if gesture == "THUMBS UP":
            if assistant_state.get_status() != AssistantStatus.CONFIRMING:
                return
            command = assistant_state.get_pending_command()
            if not command:
                return
            print("\n==============================")
            print("COMMAND CONFIRMED")
            print("==============================")
            assistant_state.clear_pending_command()
            
            # Stop confirmation speech immediately
            text_to_speech.stop()
            threading.Thread(target=self.execute_command, args=(command,), daemon=True).start()
            return

        # THUMBS DOWN
        if gesture == "THUMBS DOWN":
            if assistant_state.get_status() != AssistantStatus.CONFIRMING:
                return
            print("\n==============================")
            print("COMMAND REJECTED")
            print("==============================")

            # Stop speech immediately
            text_to_speech.stop()

            assistant_state.clear_pending_command()
            assistant_state.set_status(AssistantStatus.ACTIVATED)
            
            listener_service.start()
            return

    # =====================================================

    def start(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)

            # =====================================================
            # OCR Scan Overlay
            # =====================================================
            if assistant_state.is_ocr_scan_active():
                countdown = assistant_state.update_ocr_countdown()

                # Draw rectangle
                h, w = frame.shape[:2]

                x1 = int(w * 0.20)
                y1 = int(h * 0.15)

                x2 = int(w * 0.80)
                y2 = int(h * 0.85)

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    3,
                )

                cv2.putText(
                    frame,
                    f"Scanning in {countdown}",
                    (x1, y1 - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )

                # Wait until countdown finishes
                if countdown <= 0:
                    crop = frame[y1:y2, x1:x2].copy()
                    crop = cv2.flip(crop, 1)
                    assistant_state.set_ocr_capture(crop)
                    assistant_state.stop_ocr_scan()
                    print("Document Captured")

            assistant_state.set_current_frame(frame)
            camera_service.set_frame(frame)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            gesture = ""
            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]
                self.mp_draw.draw_landmarks(frame, hand, self.mp_hands.HAND_CONNECTIONS)
                gesture = self.recognize_gesture(hand.landmark)

            current_time = time.time()

            # Stable Gesture Detection
            if gesture != self.current_gesture:
                self.current_gesture = gesture
                self.gesture_start_time = current_time
            else:
                if (gesture and gesture != self.last_executed and 
                    current_time - self.gesture_start_time >= self.hold_time):
                    self.process_gesture(gesture)
                    self.last_executed = gesture

            if gesture == "":
                self.current_gesture = ""
                self.last_executed = ""

            # UI
            cv2.putText(frame, f"Gesture : {gesture}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Status : {assistant_state.get_status()}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

            # Confirmation banner
            if assistant_state.get_status() == AssistantStatus.CONFIRMING:
                command = assistant_state.get_pending_command()
                cv2.rectangle(frame, (10, 100), (900, 220), (40, 40, 40), -1)
                cv2.putText(frame, "VOICE COMMAND", (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                cv2.putText(frame, command, (20, 165), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, "Thumbs Up = Execute", (20, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(frame, "Thumbs Down = Speak Again", (320, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow("VisionAssist AI", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()