from pathlib import Path

import cv2

from google import genai
from google.genai import types

from app.config import settings
from app.services.assistant_state import assistant_state


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

        frame = assistant_state.get_current_frame()

        if frame is None:
            return None

        cv2.imwrite(
            str(self.image_path),
            frame,
        )

        print("Using current camera frame.")

        return self.image_path

    # ----------------------------------------------------

    def describe_scene(self):

        image_path = self.capture_image()

        if image_path is None:
            return "Camera frame not available."

        with open(image_path, "rb") as image:

            image_bytes = image.read()

        prompt = """
You are VisionAssist AI for visually impaired users.

Describe the surroundings briefly.

Rules:
- Maximum 3-4 short sentences.
- Mention important objects.
- Mention people if present.
- Mention furniture if present.
- Mention obstacles if present.
- Mention readable text if clearly visible.
- Do NOT describe facial expressions.
- Do NOT describe clothing.
- Keep the answer concise.
"""

        try:

            response = self.client.models.generate_content(

                model="gemini-2.5-flash",

                contents=[

                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type="image/jpeg",
                    ),

                    prompt,

                ],

            )

            if (
                response is None
                or response.text is None
                or not response.text.strip()
            ):
                return "I couldn't understand the scene."

            return response.text.strip()

        except Exception as e:

            print("\nVision Error:")
            print(e)

            return "Sorry, Vision AI is temporarily unavailable."


vision_tool = VisionTool()