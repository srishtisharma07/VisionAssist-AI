import cv2
import easyocr


class OCRTool:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False,
        )

    def read_image(self, image):

        results = self.reader.readtext(image)

        text = ""

        for result in results:

            text += result[1] + "\n"

        return text.strip()


ocr_tool = OCRTool()