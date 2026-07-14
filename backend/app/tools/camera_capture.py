import cv2
import os
import tempfile


class CameraCapture:

    def capture_image(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            return None

        print("\n================================")
        print("SPACE -> Capture Image")
        print("ESC   -> Cancel")
        print("================================\n")

        image_path = None

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
                "VisionAssist Camera",
                frame,
            )

            key = cv2.waitKey(1) & 0xFF

            if key == 32:

                fd, path = tempfile.mkstemp(
                    suffix=".jpg"
                )

                os.close(fd)

                cv2.imwrite(
                    path,
                    frame,
                )

                image_path = path

                break

            elif key == 27:

                break

        cap.release()

        cv2.destroyAllWindows()

        return image_path


camera_capture = CameraCapture()