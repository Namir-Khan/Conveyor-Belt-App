from flask import Flask, jsonify, render_template
from camera import Camera
from detector import Detector
from configLoader import ConfigLoader

import threading
import time

app = Flask(__name__)

config = ConfigLoader()
camera_ip = config.get_camera_ip()
model_path = config.get_model_path()
wait_time = config.get_wait_time()

camera = Camera.get_instance(camera_ip)
detector = Detector(model_path)

latest_result = {"prediction": None}
detection_active = False

def periodic_detection(interval = wait_time):
    global detection_active, latest_result
    while detection_active:
        frame = camera.capture_frame()
        if frame is not None:
            prediction = detector.detect(frame)
            latest_result["prediction"] = prediction
        time.sleep(interval)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_once')
def detect_once():
    frame = camera.capture_frame()
    if frame is not None:
        prediction = detector.detect(frame)
        return jsonify({"prediction": prediction})
    return jsonify({"prediction": "No frame"}), 500

@app.route('/start_detection')
def start_detection():
    global detection_active
    if not detection_active:
        detection_active = True
        threading.Thread(target=periodic_detection, daemon=True).start()
    return jsonify({"status": "started"})

@app.route('/stop_detection')
def stop_detection():
    global detection_active
    detection_active = False
    return jsonify({"status": "stopped"})

@app.route('/latest')
def get_latest():
    return jsonify(latest_result)

if __name__ == '__main__':
    app.run(debug=True)
