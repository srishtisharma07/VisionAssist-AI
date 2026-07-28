import os
import tempfile
import threading
import pygame
from gtts import gTTS

class TextToSpeech:

    def __init__(self):
        pygame.mixer.init()
        self.current_file = None
        self.lock = threading.Lock()

    # -----------------------------------------

    def speak(self, text: str, on_complete=None):
        if not text:
            return

        import threading

        thread = threading.Thread(
            target=self._play_audio,
            args=(text, on_complete),
            daemon=True,
        )

        thread.start()

    # -----------------------------------------

    def _play_audio(self, text: str, on_complete=None):
        self.stop()

        fd, path = tempfile.mkstemp(suffix=".mp3")
        os.close(fd)

        try:
            tts = gTTS(
                text=text,
                lang="en",
            )

            tts.save(path)

            self.current_file = path

            pygame.mixer.music.load(path)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)

        finally:
            pygame.mixer.music.stop()

            if os.path.exists(path):
                try:
                    os.remove(path)
                except:
                    pass

            self.current_file = None

            if on_complete:
                on_complete()

    # -----------------------------------------

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()


text_to_speech = TextToSpeech()