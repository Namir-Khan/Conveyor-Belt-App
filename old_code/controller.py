import time
import json
from camera import Camera
from ultralytics import YOLO

class SystemController:
    def __init__(self, modelPath, cameraIp, waitTime):
        # self.modelPath = modelPath
        self.camera = Camera(cameraIp)
        self.waitTime = waitTime
        self.yoloModel = YOLO(modelPath)

    def run(self):
        while True:
            frame = self.camera.capture_frame()
            if frame is None:
                continue

            results = self.yoloModel(frame, conf=0.4, save=False, show=False, verbose=False)
            if results[0].boxes.cls.numel() > 0:
                box_predicted = results[0].boxes.cls[0].item()
                print(f"Predicted Class: {box_predicted}")
            else:
                print("No object detected.")

            with open("status.json", "w") as f:
                json.dump({"prediction": box_predicted}, f)

            time.sleep(self.waitTime)