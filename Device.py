import serial
from queue import Queue

class Device():
    def __init__(self, name, portNumber, sensorType, minVal, maxLength, queuePar):
        self.name = name                                                                                                    # Custom name of device. For example: Living room
        self.status = 1                                                                                                     # 1 = rolled up, 0 = rolled down
        self.portNumber = portNumber                                                                                        # Port used to connect to device
        self.sensorType = sensorType                                                                                        # Type of sensor used in device
        self.maxLength = maxLength                                                                                          # Maximun roll distance of the shutter
        self.rollPercentage = 0                                                                                             # Percentage shutter has rolled out. Between 0 and 100
        self.queue = queuePar
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

    def getStatus(self):
        if self.status == 1:  # If status of device = 1, then return Rolled Up
            return "Rolled up"
        elif self.status == 0:  # If status of device = 0, then return Rolled Down
            return "Rolled down"

    def receive(self):
        data = self.connection.read()
        if not data:
            return
        # print_status('Received message')
        # print(data)
        self.transmission = int(ord(data))
        # print(transmission)
        value = 0

        if self.transmission != 0xff:
            # print(self.transmission)
            return
        # pass

        # print_status('Transmission received. Sending confirmation...')
        # print('First transmission: ', self.transmission)
        while True:
            # print_status('Preparing to receive multiple transmissions')
            data = self.connection.read()
            # print(data)
            self.transmission = int(ord(data))
            # print(self.transmission)

            if self.transmission == 0b01000000:
                # print_status('Transmission received: Arduino is trying to send data')
                while True:
                    data = self.connection.read()
                    self.transmission = int(ord(data))
                    # print('Data transmission: ', self.transmission)
                    if self.transmission == 0b01110000:
                        # print_status('Nothing more to do')
                        break
                    else:
                        value += self.transmission

                # print_status('Preparing to read received data')
                value /= 10
                self.queue.put(value)
                break
            elif self.transmission == 0b01010001:
                print("Shutter rolled up")
                self.status = 1
                break
            elif self.transmission == 0b01010000:
                print("Shutter rolled down")
                self.status = 0
                break
            else:
                break

    def getData(self):
        return self.queue.get()

# Test code
"""port = 'COM5'

try:
    q = Queue()
    shutter = Device("Attic", port, "Light", 0, 1.50, q)
    print("Connection established on {0}".format(port))

    while True:
        print(shutter.receive())

except Exception as e:
    print(e)"""
