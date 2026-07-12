import os
import tempfile
import threading

from gtts import gTTS
import pygame


class TextToSpeech:

    def __init__(self):

        pygame.mixer.init()

        self.current_file = None

        self.lock = threading.Lock()

    def speak(self, text: str):

        if not text:
            return

        thread = threading.Thread(
            target=self._play_audio,
            args=(text,),
            daemon=True,
        )

        thread.start()

    def _play_audio(self, text: str):

        try:

            with self.lock:

                self.stop()

                fd, path = tempfile.mkstemp(suffix=".mp3")
                os.close(fd)

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

            with self.lock:

                pygame.mixer.music.stop()

                if (
                    self.current_file
                    and os.path.exists(self.current_file)
                ):
                    try:
                        os.remove(self.current_file)
                    except Exception:
                        pass

                self.current_file = None

    def stop(self):

        pygame.mixer.music.stop()


text_to_speech = TextToSpeech()