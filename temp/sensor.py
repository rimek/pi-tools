import time
import os

from temperature import Temperature
from config import DEVICES_DIR

class Sensor(object):
    def __init__(self, sensorId, sensorName):
        self.path = os.path.join(DEVICES_DIR, sensorId, 'w1_slave')
        self.id = sensorId
        self.name = sensorName

    def read(self, path=None):
        #f6 01 4b 46 7f ff 0a 10 eb : crc=eb YES
        #f6 01 4b 46 7f ff 0a 10 eb t=31375

	path = self.path if not path else path

        try:
            sensor = open(path, "r")
            data = sensor.readlines()
            sensor.close()

            if data[0].strip()[-3:] == "YES":
                equals_pos = data[1].find("t=")
                if equals_pos != -1:
                    data = data[1][equals_pos+2:]
                    temperature = Temperature(data)
                else:
                    raise IndexError
            else:
                raise IndexError
        except IndexError:
            print 'error'

	return temperature


