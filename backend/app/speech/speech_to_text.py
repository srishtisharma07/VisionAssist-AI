import speech_recognition as sr


class SpeechToText:

    def __init__(self):

        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\nListening...\n")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1,
            )

            audio = self.recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15,
            )

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"Recognized: {text}")

            return text

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            return ""

        except Exception:

            return ""


speech_to_text = SpeechToText()