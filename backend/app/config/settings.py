from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        if not self.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file."
            )


settings = Settings()