#!/usr/bin/python2.7
import sys, time
import socket
from setproctitle import setproctitle
from SimpleXMLRPCServer import SimpleXMLRPCServer

import netifaces

from process import Process
from config import RPC_HOST, RPC_PORT


DEBUG=True

class PiTemp(object):
    rpc_server = None
    controller = None

    def __init__(self):
        setproctitle('pi-temp')

        if DEBUG:
            print('Starting...')
        self.controller = Process(300) # 5 minutes
        self.controller.start()

        self.rpc_server()
        self.loop()

    def get_ip(self):
        try:
            return netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
        except:
            return RPC_HOST

    def rpc_server(self):
        try:
            self.rpc_server = SimpleXMLRPCServer((self.get_ip(), RPC_PORT))
        except socket.error, e:
            self.terminate('RPC server: %s' % e)

        self.rpc_server.register_function(
                self.controller.rpc_get_sensor_value,
                "temperature"
                )
        self.rpc_server.register_function(
                self.controller.rpc_get_values,
                "temperatures"
                )
        self.rpc_server.register_function(
                self.controller.rpc_timestamp,
                "timestamp"
                )
        self.rpc_server.register_function(
                self.controller.rpc_get_log,
                "log"
                )

    def loop(self):
        try:
            self.rpc_server.serve_forever()
        except KeyboardInterrupt:
            self.terminate('Keyboard cancelled')

    def terminate(self, message):
        print "(Error) %s" % message if DEBUG else 'Quit'

        self.controller.stop()
        self.controller.join()

        sys.exit()


if __name__ == '__main__':
    PiTemp()
