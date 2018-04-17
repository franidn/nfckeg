#!/usr/bin/env python
#Definim llibreries GPIO per treballar amb els pins de la raspby
import RPi.GPIO as GPIO
#Importem llibreries necesaries
import time, sys

#Definim pin BCM 17 per connectarhi el sensor de flux
FLOW_SENSOR = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Variable global per contar voltes del sensor de flux
global count
count = 0

#Funció que llegeig les voltes del pin 17 i les transfotma a litres
def countPulse(channel):
   global count
   count = count+1
   actual_liters = count/float(400)
   #print count
   print actual_liters
   return actual_liters

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)
actual_liters = actual_liters

#bucle que mante en espera perque conti fins que ho interrumpim amb CTRL+C
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
