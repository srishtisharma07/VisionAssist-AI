from pathlib import Path

import cv2

from google import genai
from google.genai import types

from app.config import settings


class VisionTool:

    def __init__(self):

        self.image_path = Path("uploads/captured_image.jpg")

        self.image_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    # ----------------------------------------------------

    def capture_image(self):

        camera = cv2.VideoCapture(0)

        if not camera.isOpened():

            return None

        success, frame = camera.read()

        camera.release()

        if not success:

            return None

        cv2.imwrite(
            str(self.image_path),
            frame,
        )

        return self.image_path

    # ----------------------------------------------------

    def describe_scene(self):

        image_path = self.capture_image()

        if image_path is None:

            return "Unable to capture image."

        with open(image_path, "rb") as image:

            image_bytes = image.read()

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=[

                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/jpeg",
                ),

                "Describe everything visible in this image in detail."

            ]

        )

        return response.text


vision_tool = VisionTool()