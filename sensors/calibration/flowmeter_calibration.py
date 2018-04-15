#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global count
count = 0

def countPulse(channel):
   global count
   count = count+1
   actual_liters = count/float(400)
   print count
   print actual_liters

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
