#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
from main import Sensor
import time

class rfid(Sensor):
    def __init__(self,name):
        super(rfid, self).__init__(name)
        #Create an object with MFRC522 properties
        self.MIFAREReader = MFRC522.MFRC522()

    #This function capture ID of card
    def get_uid(self):
        # Scan for cards
        (status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        # If a card is found
        if status == self.MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        (status,uid) = self.MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == self.MIFAREReader.MI_OK:

            # Print UID
            print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

            # Select the scanned tag
            self.MIFAREReader.MFRC522_SelectTag(uid)
            return uid
    #This function permits read data in card
    def read_card(self, uid):

        data = self.MIFAREReader.MFRC522_Read(uid)
        return data

    #This function permits write info at card
    def write_card(self, uid, data):

        self.MIFAREReader.MFRC522_Write(uid, data)

if __name__ == "__main__":
    a = rfid("eee")    
    while True:
        a = rfid("eee")
        uid = a.get_uid()
        time.sleep(1)
