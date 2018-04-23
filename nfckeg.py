import time
import pprint as pp
import notifications
import sensors

class nfckeg(object):
    #nfckeg is a beer liters identification system
    def __init__(self):
        super(nfckeg, self).__init__()
        self.my_sensors_names = ["flowsensor", "nfcsensor"]
        self.uidlitres = {}
        global info

    def create_sensors(self):
        self.flow_sensor = sensors.flow_sensor.flowsensor(self.my_sensors_names[0])
        self.writepre = sensors.writepre.rfid(self.my_sensors_names[1])

    # Carguem els setups del flowsensor i del lector rfid
    def setup(self):
        self.flow_sensor.setup()
        

    #Actualitzem els valors dels sensors i els afegim a la ultima posicio d'una matriu
    def get_state(self):
        while True:
            uid = self.writepre.get_uid()
            time.sleep(1)
            if uid is not None:
                litres = self.flow_sensor.getacumulateliters()
                for uid in self.uidlitres:
                    info = ('{}:{}'.format(uid, self.litres))
                time.sleep(1)

            

    #Funcio principal que ens printa el id i els litres beguts
    def main(self):
        try:
            while True:
                estat = self.get_state()
                print ("El id: "+uidliters[1]+ "ha begut: "+uidliters[2])
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()


if __name__ == "__main__":
    sensor = nfckeg()
    sensor.create_sensors()
    sensor.setup()
    sensor.main()
