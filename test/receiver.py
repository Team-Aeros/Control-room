#!/usr/bin/env python3

import serial
import time

class Device():
    def __init__(self, name, portNumber, sensorType, minVal, maxLength):
        self.name = name                                                                                                    # Custom name of device. For example: Living room
        self.status = 1                                                                                                     # 1 = rolled up, 0 = rolled down
        self.portNumber = portNumber                                                                                        # Port used to connect to device
        self.sensorType = sensorType                                                                                        # Type of sensor used in device
        self.maxLength = maxLength                                                                                          # Maximun roll distance of the shutter
        self.rollPercentage = 0                                                                                             # Percentage shutter has rolled out. Between 0 and 100

        if minVal != 0:                                                                                                     # If custom value is given use that value
            self.minVal = minVal        
        elif self.sensorType == "Light":                                                                                    # If no custom value is given and sensor type = "Light" use default light value
            self.minVal = 50
        elif self.sensorType == "Temp":                                                                                     # If no custom value is given and sensor type = "Temp" use default light value
            self.minVal = 22

        self.establishConnection()                                                                                          # Establish connection using given port
        # Send settings to arduino

    # Connection code
    def establishConnection(self):
        self.connection = serial.Serial(self.portNumber, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.2)     # Opens port to device.

    def transmit(self, message):
        self.connection.write(message)

    def receive(self):
        data = self.connection.read()

        if not data:
            return

        transmission = int(ord(data))

        if transmission == 0xFF or transmission == 0b01110000 or transmission == 64:
            return

        print(transmission)

# Test code
port = '/dev/ttyACM0'

try:
    shutter = Device("Attic", port, "Light", 0, 1.50)
    print("Connection established on {0}".format(port))

    while True:
        shutter.receive()

except Exception as e:
    print(e)