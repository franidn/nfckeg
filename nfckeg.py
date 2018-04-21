import time
import pprint as pp
import notifications
import sensors

class nfckeg(object):
    #nfckeg is a beer liters identification system
    def __init__(self):
        super(nfckeg, self).__init__()
        self.my_sensors_names = ["flowsensor", "nfcsensor"]

        #FALTA MERDA QUE NO ENTENC


    def create_sensors(self):
        sensor.flow_sensor(self.my_sensors_names(1))
        sensor.writepre(self.my_sensors_names(2))

    # Carguem els setups del flowsensor i del lector rfid
    def setup(self):
        self.flow_sensor.setup()
        self.writepre.setup()
        self.uidliters = [[0,0]]
        self.a = 0

    #Actualitzem els valors dels sensors i els afegim a la ultima posicio d'una matriu
    def get_state(self):
        self.a = 1
        while a == 1:
            uid = writepre.get_uid
            time.sleep(1)
            if uid is not None:
                litres = flow_sensor.getacumulateliters()
                self.uidliters = append(self.uidliters["uid",litres])
                time.sleep(1)
                return uidliters
                a = 0

    #Funcio principal que ens printa el id i els litres beguts
    def main(self):
        try:
            while True:
                estat = self.get_state()
                print ("El id: "+uidliters(1) "ha begut: "+uidliters(2))
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()


if __name__ == "__main__":
    sensor = Sensor()
    sensor.main()
