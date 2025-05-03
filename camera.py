import cv2

class Camera:
    def __init__(self, cameraIp):
        self.cap = cv2.VideoCapture(cameraIp)
        self.warm_up()

    def warm_up(self):
        for _ in range(5):
            self.cap.read()

    def capture_frame(self):
        self.cap.grab()
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could Not Capture Image")
        return frame

    def release(self):
        self.cap.release()