import cv2
import easyocr


class OCRTool:

    def __init__(self):
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False,
        )

    def detect_document(self, image):
        # Convert to grayscale if necessary
        if len(image.shape) == 3:
            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY,
            )
        else:
            gray = image.copy()

        # Blur
        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0,
        )

        # Edge Detection
        edges = cv2.Canny(
            blurred,
            75,
            200,
        )

        # Find contours
        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        contours = sorted(
            contours,
            key=cv2.contourArea,
            reverse=True,
        )

        for contour in contours[:5]:
            perimeter = cv2.arcLength(
                contour,
                True,
            )

            approx = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True,
            )

            # Document usually has 4 corners
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)

                # Ignore tiny rectangles
                if w < 200 or h < 200:
                    continue

                cropped = image[
                    y:y + h,
                    x:x + w,
                ]

                print("Document detected.")
                return cropped

        print("No document detected.")
        return image

    def read_image(self, image):
        image = self.detect_document(image)

        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        # Upscale
        gray = cv2.resize(
            gray,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC,
        )

        # Very light denoising
        gray = cv2.GaussianBlur(
            gray,
            (3, 3),
            0,
        )

        # Save for debugging
        cv2.imwrite("ocr_processed.jpg", gray)

        # OCR
        results = self.reader.readtext(
            gray,
            detail=0,
            paragraph=False,
            width_ths=0.7,
            decoder="beamsearch",
        )

        text = "\n".join(results)

        return text.strip()


# Usage
ocr_tool = OCRTool()
# result = ocr_tool.read_image(cv2.imread("your_image.jpg"))