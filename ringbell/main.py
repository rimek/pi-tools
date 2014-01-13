#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time
import os
from setproctitle import setproctitle

pin = 22

def bell(pin):
  time.sleep(0.05)
  if not GPIO.input(buttonPin):
    os.system("mpg123 /nfs/domek/plc/dzwonek.mp3")

def initialize():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin,GPIO.IN)

  GPIO.add_event_detect(22, GPIO.FALLING, callback=bell, bouncetime=300)
  #GPIO.add_event_callback(22, callback=bell, bouncetime=300)

if __name__ == '__main__':
  setproctitle('pi-ringbell')
  initialize()

  while True:
    time.sleep(0.05)

