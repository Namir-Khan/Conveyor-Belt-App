from configLoader import ConfigLoader
from controller import SystemController

def main():
    config = ConfigLoader()
    cameraList = config.get_camera_ips()
    modelPath = config.get_model_path()
    waitTime = config.get_wait_time()

    controller1 = SystemController(modelPath, cameraIp = cameraList[0], waitTime = waitTime)

    try:
        controller1.run()
    except KeyboardInterrupt:
        print("Exiting system...")
    finally:
        controller1.cleanup()

if __name__ == "__main__":
    main()