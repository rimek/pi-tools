import threading
import time
import sqlite3

from config import devices
from sensor import Sensor


class ProcessDB(object):
    db_path = '/var/pi/temp.sqlite3'

    def __init__(self):
        self.initialize_db()

    def connect(self):
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()

    def disconnect(self):
        self.cursor.close()
        self.db.close()

    def initialize_db(self):
        self.connect()
        init_sql = 'CREATE TABLE IF NOT EXISTS temp_log (date text, name text, value text)'
        self.cursor.execute(init_sql)
        self.db.commit()
        self.disconnect()

    def insert_temp(self, name, value):
        self.connect()
        self.cursor.execute("INSERT INTO temp_log VALUES(?,?,?)", (
            str(time.time()),
            str(name),
            str(value)
        ))
        self.db.commit()
        self.disconnect()

    def read_temp(self):
        self.connect()
        values = self.cursor.execute("SELECT * FROM temp_log").fetchall()
        self.disconnect()
        return values


class ProcessData(object):
    timestamp = None
    db = None
    data = {}

    def __init__(self):
        self.db = ProcessDB()

    def set(self, sensor_name, value):
        self.timestamp = time.time()
        self.data[sensor_name] = value
        self.save_log(sensor_name, value)

    def save_log(self, sensor, value):
        self.db.insert_temp(sensor, value)

    def get(self, sensor_name):
        try:
            return self.data[sensor_name]
        except KeyError, e:
            return '--'


    def get_all(self):
        return self.data

    def get_log(self):
        return self.db.read_temp()



class Process(threading.Thread):
    data = ProcessData()

    def __init__(self, timeToSleep):
        threading.Thread.__init__(self)
        self.running = False
        self.sleepTime = timeToSleep

    def run(self):
        self.running = True
        sensors = [Sensor(id,name) for (id,name) in devices()]

        while(self.running):
            for sensor in sensors:
                self.data.set(sensor.name, sensor.read().C)

            time.sleep(self.sleepTime)
        self.running = False

    def stop(self):
        self.running = False

    def rpc_get_values(self):
        return self.data.get_all()

    def rpc_get_sensor_value(self, sensor_name):
        return self.data.get(sensor_name)

    def rpc_timestamp(self):
        return self.data.timestamp

    def rpc_get_log(self):
        return self.data.get_log()
