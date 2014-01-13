#!/usr/bin/python

from sensor import TempSensorController
       
tempcontrol = TempSensorController("28-0000043fd3b3", 1)

try:
    print("Starting temp sensor controller")
    #start up temp sensor controller
    tempcontrol.start()
    #loop forever, wait for Ctrl C
    while(True):
        print tempcontrol.temperature.C
        print tempcontrol.temperature.F
        time.sleep(5)
#Ctrl C
except KeyboardInterrupt:
    print "Cancelled"

#Error
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

#if it finishes or Ctrl C, shut it down
finally:
    print "Stopping temp sensor controller"
    #stop the controller
    tempcontrol.stopController()
    #wait for the tread to finish if it hasn't already
    tempcontrol.join()
   
print "Done"
