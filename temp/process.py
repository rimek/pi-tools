import threading
import time

from config import devices
from sensor import Sensor


class Process(threading.Thread):
    def __init__(self, timeToSleep):
        threading.Thread.__init__(self)
        self.running = False
        self.sleepTime = timeToSleep
        self.data = {}

    def run(self):
        self.running = True
        sensors = [Sensor(id,name) for (id,name) in devices()]

        while(self.running):
            for sensor in sensors:
                self.data[sensor.name] = sensor.read().C
                time.sleep(self.sleepTime)
        self.running = False

    def stop(self):
        self.running = False

    def rpc_data(self):
        return self.data
