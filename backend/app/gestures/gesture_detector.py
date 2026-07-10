import time
import cv2
import mediapipe as mp

from app.services.assistant_state import assistant_state


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

        # Debounce
        self.last_gesture = ""
        self.last_detection_time = 0
        self.debounce_time = 1.5

    def get_finger_states(self, landmarks):
        tips = [4, 8, 12, 16, 20]
        fingers = []

        # Thumb
        if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # Index, Middle, Ring, Pinky
        for tip in tips[1:]:
            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def recognize_gesture(self, fingers):
        thumb, index, middle, ring, pinky = fingers

        # ✋ Open Palm
        if fingers == [1, 1, 1, 1, 1]:
            return "OPEN PALM"

        # ✊ Fist
        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        # ✌ Victory
        if fingers == [0, 1, 1, 0, 0]:
            return "VICTORY"

        # 👍 Thumb Up
        if fingers == [1, 0, 0, 0, 0]:
            return "THUMBS UP"

        # 👎 Thumb Down (temporary logic)
        if fingers == [0, 1, 1, 1, 1]:
            return "THUMBS DOWN"

        return ""

    def process_gesture(self, gesture):
        current_time = time.time()

        if not gesture:
            return

        if (
            gesture != self.last_gesture
            or current_time - self.last_detection_time > self.debounce_time
        ):
            assistant_state.set_gesture(gesture)

            print(f"Detected: {gesture}")

            self.last_gesture = gesture
            self.last_detection_time = current_time

    def start(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():

            success, frame = cap.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.hands.process(rgb)

            gesture = ""

            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                    )

                    fingers = self.get_finger_states(
                        hand_landmarks.landmark
                    )

                    gesture = self.recognize_gesture(fingers)

                    self.process_gesture(gesture)

            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("VisionAssist AI", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()