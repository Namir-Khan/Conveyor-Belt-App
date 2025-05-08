import cv2

class Camera:
    _instance = None

    def __init__(self, camera_ip):
        self.cap = cv2.VideoCapture(camera_ip)
        self._warm_up()

    def _warm_up(self):
        for _ in range(5):
            self.cap.read()

    def capture_frame(self):
        self.cap.grab()
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()

    @classmethod
    def get_instance(cls, camera_ip):
        if cls._instance is None:
            cls._instance = cls(camera_ip)
        return cls._instance