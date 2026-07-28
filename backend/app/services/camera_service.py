import threading


class CameraService:

    def __init__(self):

        self.frame = None
        self.lock = threading.Lock()

    def set_frame(self, frame):

        with self.lock:
            self.frame = frame.copy()

    def get_frame(self):

        with self.lock:

            if self.frame is None:
                return None

            return self.frame.copy()


camera_service = CameraService()