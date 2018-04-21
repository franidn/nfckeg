#Definim llibreries GPIO per treballar amb els pins de la raspby
import RPi.GPIO as GPIO
#Importem llibreries necesaries
import time, sys

from main import Sensor

class flowsensor(Sensor):

    def __init__(self,name):
        super(flowsensor, self).__init__(name)

    #Configuracio interna del sensor
    def setup(self):
        #Defenim pin BCM17 per conectar el sensor de flux
        FLOW_SENSOR_PIN = 17
        #Diem a la raspberry que ens referirem als pins com BCM
        GPIO.setmode(GPIO.BCM)
        #Definim en quin pin, quina funcio fara el pin i posem en down la resistencia interna del pin
        GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #Cridem la funcio countPulse quan detectem una senyal al pin espentan
        GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.RISING, callback=self.countPulse)
        #Inicialitzem una varialble global per contar voltes del sensor de flux
        self.count = 0

    #Funcio que cada cop que es executada suma 1
    #Es cridada cada cop que la raspberry rep un pols, com que treballem amb un sensor d'efecte hall cada cop que dona una volta emet un pols
    #Amb el contador count ens limitem a cada cop que el sensor emet un pols sumarli un a la variable
    def countPulse(self, channel):
       self.count = self.count+1

    #Previament calibrat el sensor sabem que cada 400 voltes es un litre
    #Amb aquesta funcio obtenim els litres que pasen pel flowsensor
    def getacumulateliters(self):
       acumulate_liters = self.count/float(400)
       print acumulate_liters
       return acumulate_liters


    def resetliters(self):
        self.count = 0
        self.acumulate_liters = 0

#Funcio que s'executa al executar la classe, dins conte un bucle que crida cada segon la funcio getliters
if __name__ == "__main__":
    s = flowsensor("eeee")
    s.setup()
    while True:
        try:
            time.sleep(1)
            s.getacumulateliters()
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
