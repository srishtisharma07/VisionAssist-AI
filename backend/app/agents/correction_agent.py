from google import genai

from app.config import settings
from app.prompts.correction_prompt import CORRECTION_PROMPT


class CorrectionAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    # --------------------------------------------------

    def correct(self, command: str):

        if not command:
            return command

        prompt = f"""
{CORRECTION_PROMPT}

User Command:

{command}
"""

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            corrected = response.text.strip()

            print("\n==============================")
            print("COMMAND CORRECTION")
            print("==============================")
            print("Original :", command)
            print("Corrected:", corrected)
            print("==============================\n")

            return corrected

        except Exception as e:

            print("Correction Agent Error:", e)

            return command


correction_agent = CorrectionAgent()