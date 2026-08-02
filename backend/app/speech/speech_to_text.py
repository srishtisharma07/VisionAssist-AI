import re
import speech_recognition as sr

class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        # Better defaults for voice commands
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.4
        self.recognizer.phrase_threshold = 0.3

    # ----------------------------------------
    # Normalizes voice input for consistent command parsing
    # ----------------------------------------
    def clean_command(self, text):
        text = text.lower().strip()
        text = re.sub(r"\s+", " ", text)

        replacements = {
            "folder name": "folder named",
            "file name": "file named",
            "folder called": "folder named",
            "file called": "file named",
            "downloads folder": "downloads",
            "desktop folder": "desktop",
            "pictures folder": "pictures",
            "documents folder": "documents",
            "dot txt": ".txt",
            "text file": ".txt",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    # ----------------------------------------

    def listen(self):
        with sr.Microphone() as source:
            print("\nListening...\n")

            # Reduce background noise calibration time
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5,
            )

            audio = self.recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10,
            )

        try:
            text = self.recognizer.recognize_google(
                audio,
                language="en-IN",
            )

            text = self.clean_command(text)

            print(f"Recognized: {text}")

            return text

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

        except Exception as e:
            print(f"An error occurred: {e}")
            return ""


speech_to_text = SpeechToText()