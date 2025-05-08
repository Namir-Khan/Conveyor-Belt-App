from ultralytics import YOLO

class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, conf=0.4, save=False, show=False, verbose=False)
        if results and results[0].boxes.cls.numel() > 0:
            return int(results[0].boxes.cls[0].item())
        return "No object"