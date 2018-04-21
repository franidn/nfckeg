#!/usr/bin/env python
#Definim llibreries GPIO per treballar amb els pins de la raspby
import RPi.GPIO as GPIO
#Importem llibreries necesaries
import time, sys

from main import Sensor

class flowsensor(Sensor):
    def __init__(self,name):
        super(flowsensor, self).__init__(name)
#Defenim pin BCM17 per conectar el sensor de flux
        FLOW_SENSOR = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=self.countPulse)
#Varialble global per contar voltes del sensor de flux
        self.count = 0


#Funcio que llegeig les voltes del pin 17 i les transforma a litres
    def countPulse(self, channel):
       self.count = self.count+1

    def getliters(self):
       actual_liters = self.count/float(400)
       #print count
       print actual_liters
       return actual_liters

    #bucle que mante en espera perque conti fins que ho interrumpim amb CTRL+C

if __name__ == "__main__":
    s = flowsensor("eeee")
    while True:
        try:
            s.getliters()
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
