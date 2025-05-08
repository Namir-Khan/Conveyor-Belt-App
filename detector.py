from ultralytics import YOLO

class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, conf=0.4, save=False, show=False, verbose=False)

        if results:
            boxes = results[0].boxes

        # if results and results[0].boxes.cls.numel() > 0:
        #     class_id = int(results[0].boxes.cls[0].item())

        if boxes.cls.numel() > 0:
            max_conf_idx = boxes.conf.argmax().item()
            class_id = int(boxes.cls[max_conf_idx].item())
            class_name = self.model.names[class_id]
        else:
            class_name = "No object"

        return class_name