import time
import pprint as pp
import notifications
import sensors

class nfckeg(object):
    #nfckeg is a beer liters identification system
    def __init__(self):
        super(nfckeg, self).__init__()
        self.my_sensors_names = ["flowsensor", "nfcsensor"]
        self.info = {}
        

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
            print(uid)
            time.sleep(1)
            if uid is not None:
                self.info = {uid:0}
                litres = 0
                litres_antes = -1
                while litres != litres_antes:
                    litres = self.flow_sensor.getacumulateliters()
                    litres_antes = litres
                    time.sleep(3)
                    litres = self.flow_sensor.getacumulateliters()
                    if litres == litres_antes: 
                        self.info = {uid:litres_antes}
                        self.flow_sensor.resetliters()
                time.sleep(1)
                print(self.info)

    #Funcio principal que ens printa el id i els litres beguts
    def main(self):
        try:
            while True:
                estat = self.get_state()
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()


if __name__ == "__main__":
    sensor = nfckeg()
    sensor.create_sensors()
    sensor.setup()
    sensor.main()
