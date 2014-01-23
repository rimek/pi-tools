#!/usr/bin/python2.7

import time
import xmlrpclib
from setproctitle import setproctitle
from SimpleXMLRPCServer import SimpleXMLRPCServer

from process import Process
from config import RPC_HOST, RPC_PORT


DEBUG=True

server = SimpleXMLRPCServer((RPC_HOST, int(RPC_PORT)))
setproctitle('pi-temp')
controller = Process(2)

try:
    if DEBUG:
        print('Starting...')

    controller.start()

    server.register_function(controller.rpc_data, "temperatures")
    server.serve_forever()

    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print('Cancelled')

controller.stop()
controller.join()

if DEBUG:
   print('Quit')
