#!/usr/bin/python2.7

import RPi.GPIO as GPIO
import time
import os

def buttonEventHandler(pin):
  os.system("mpg123 /nfs/domek/plc/dzwonek2.mp3")


#adjust for where your switch is connected
buttonPin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

GPIO.add_event_detect(22,GPIO.FALLING)
GPIO.add_event_callback(22,buttonEventHandler,100)

while True:
  time.sleep(0.05)

  #  #assuming the script to call is long enough we can ignore bouncing
  #  if not GPIO.input(buttonPin):
  #    #this is the script that will be called (as root)
  #    os.system("mpg123 /nfs/domek/plc/dzwonek.mp3")
  #    time.sleep(0.35)
