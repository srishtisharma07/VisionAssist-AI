import time

import cv2
import mediapipe as mp

from app.services.assistant_state import assistant_state
from app.services.assistant_status import AssistantStatus
from app.services.listener_service import listener_service
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

        self.last_gesture = ""

        self.gesture_locked = False

    # ----------------------------------------------------

    def get_finger_states(self, landmarks):

        fingers = []

        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        for tip in [8, 12, 16, 20]:

            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    # ----------------------------------------------------

    def recognize_gesture(self, fingers):

        if fingers == [1, 1, 1, 1, 1]:
            return "OPEN PALM"

        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        if fingers == [0, 1, 0, 0, 0]:
            return "INDEX"

        if fingers == [0, 1, 1, 0, 0]:
            return "VICTORY"

        if fingers == [1, 0, 0, 0, 0]:
            return "THUMBS UP"

        if fingers == [0, 1, 1, 1, 1]:
            return "THUMBS DOWN"

        return ""

    # ----------------------------------------------------

    def process_gesture(self, gesture):

        if not gesture:
            return

        assistant_state.set_gesture(gesture)

        print(f"\nDetected Gesture: {gesture}")

        if gesture == "OPEN PALM":

            assistant_state.activate()

            print("\n==============================")
            print("Assistant Activated")
            print("==============================")

        elif gesture == "FIST":

            text_to_speech.stop()

            assistant_state.deactivate()

            print("\n==============================")
            print("Assistant Deactivated")
            print("==============================")

        elif gesture == "INDEX":

            if assistant_state.get_status() != AssistantStatus.ACTIVATED:

                print("Assistant is inactive.")

                return

            print("\n==============================")
            print("Voice Assistant Started")
            print("==============================")

            listener_service.start()

    # ----------------------------------------------------

    def start(self):

        cap = cv2.VideoCapture(0)

        while cap.isOpened():

            success, frame = cap.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB,
            )

            results = self.hands.process(rgb)

            gesture = ""

            if results.multi_hand_landmarks:

                hand = results.multi_hand_landmarks[0]

                self.mp_draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS,
                )

                fingers = self.get_finger_states(
                    hand.landmark
                )

                gesture = self.recognize_gesture(
                    fingers
                )

                if not self.gesture_locked:

                    self.process_gesture(
                        gesture
                    )

                    if gesture:
                        self.gesture_locked = True

            else:

                self.gesture_locked = False

            cv2.putText(
                frame,
                f"Gesture : {gesture}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Status : {assistant_state.get_status()}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2,
            )

            cv2.imshow(
                "VisionAssist AI",
                frame,
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        cap.release()

        cv2.destroyAllWindows()