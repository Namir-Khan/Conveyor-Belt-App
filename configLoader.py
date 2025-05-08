import configparser
import os

class ConfigLoader:
    def __init__(self, config_path="resources/config.properties"):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_camera_ip(self):
        return [
            self.config.get("CAMERAS", "camera1")
        ]

    def get_serial_port(self):
        return self.config.get("SERIAL", "port")

    def get_model_path(self):
        return self.config.get("MODEL", "path")
    
    def get_wait_time(self):
        return self.config.getint("SYSTEM", "waitTime")