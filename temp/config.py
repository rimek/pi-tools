import glob
import os

RPC_HOST = '192.168.13.123'
RPC_PORT = '10000'

DEVICES_DIR = "/sys/bus/w1/devices/"

DEVICES_NAMES = (
    ('28-00000440436b', 'salon'),
    ('28-0000043f470d', 'office'),
    ('28-0000043f5dd8', 'entry')
)

def devices():
    devs = glob.glob(os.path.join(DEVICES_DIR, '28*'))
    result = []

    return [deviceName(sid) for sid in [os.path.basename(dev) for dev in devs]]

def deviceName(id):
    for (sid,name) in DEVICES_NAMES:
        if sid == id:
            return (sid, name)
    return (id, id)



