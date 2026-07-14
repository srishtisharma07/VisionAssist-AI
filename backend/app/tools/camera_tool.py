import cv2

from app.tools.ocr_tool import ocr_tool


class CameraTool:

    def capture_text(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            return None

        print("\n===================================")
        print("SPACE -> Capture Document")
        print("ESC   -> Cancel")
        print("===================================\n")

        extracted_text = None

        while True:

            success, frame = cap.read()

            if not success:
                continue

            cv2.putText(
                frame,
                "SPACE = Capture | ESC = Cancel",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

            cv2.imshow(
                "VisionAssist OCR",
                frame,
            )

            key = cv2.waitKey(1) & 0xFF

            if key == 32:

                extracted_text = ocr_tool.read_image(
                    frame
                )

                break

            elif key == 27:

                break

        cap.release()

        cv2.destroyAllWindows()

        return extracted_text


camera_tool = CameraTool()