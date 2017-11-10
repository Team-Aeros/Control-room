import serial
import time
from threading import Thread


def print_status(msg):
    print('=> Debug: {0}'.format(msg))


class Device():#Thread):

    def __init__(self, name, portNumber, sensorType, minVal, maxLength):
        #Thread.__init__(self)
        self.name = name        																							# Custom name of device. For example: Living room
        self.status = 1																										# 1 = rolled up, 0 = rolled down
        self.portNumber = portNumber																						# Port used to connect to device
        self.sensorType = sensorType																						# Type of sensor used in device
        self.maxLength = maxLength																							# Maximun roll distance of the shutter
        self.rollPercentage = 0																						        # Percentage shutter has rolled out. Between 0 and 100
        if minVal != 0:																										# If custom value is given use that value
            self.minVal = minVal
        elif self.sensorType == "Light":																					# If no custom value is given and sensor type = "Light" use default light value
            self.minVal = 50
        elif self.sensorType == "Temp":																						# If no custom value is given and sensor type = "Temp" use default light value
            self.minVal = 22

        connection = Thread(target=self.establishConnection)																							# Establish connection using given port
        connection.setDaemon(True)
        connection.start()
        #print(connection) debug
        #print("create thread:", connection.is_alive()) debug
    # Send settings to arduino

    """def run(self):
        self.establishConnection()
        self.receive()"""
    # Connection code
    def establishConnection(self):
        global hasConnection
        try:
            self.connection = serial.Serial(self.portNumber, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.5) 	# Opens port to device.
        except:
            del self
            #raise ValueError("No device connected")

    def transmit(self, message):
        self.connection.write(message)

    def receive(self):
        data = self.connection.read()

        if not data:
            # print_status('Nothing to receive')
            return

        print_status('Received message')

        transmission = int('{:08b}'.format(ord(data)),2) 																	# First transmission. Should be 0xff
        value = 0																											# Set value to 0 for receiving data

        if transmission != 0xff:																							# Starts transmission cycle
            return

        print_status('Transmission received. Sending confirmation...')
        #self.transmit(b'\x60') 																								# Send confirmation
        #print_status('Confirmation sent')

        print('First transmission: ', transmission) 																		# Used for testing remove later

        while True:
            print_status('Preparing to receive multiple transmissions')

            transmission = int('{:08b}'.format(ord(self.connection.read())),2) 												# Second transmission
            #self.transmit(b'\x60') 																							# Send confirmation
            print('Instruction: ', transmission) 																			# Used for testing remove later

            if transmission == 0b01000000: 																					# Check if transmission is sending data
                print_status('Transmission received: Arduino is trying to send data')

                while True:
                    transmission = int('{:08b}'.format(ord(self.connection.read())),2) 										# Data transmission
                    #self.transmit(b'\x60') 																					# Send confirmation
                    print('Data transmission: ', transmission) 																# Used for testing remove later

                    if transmission == 0b01110000: 																			# Check if end of transmission is received
                        print_status('Nothing more to do')
                        break
                    else:
                        value += transmission																				# Add transmitted value to value

                print_status('Preparing to read received data')
                value /= 10
                print('Received data: ', value) 																			# Used for testing remove later
                break
            elif transmission == 0b01010001:																				# Change shutter status to rolled up
                print_status('Status has been set to 1')
                self.status = 1
                break
            elif transmission == 0b01010000:																				# Change shutter status to rolled down
                print_status('Status has been set to 0')
                self.status = 0
                break

    def rollUp(self):
        self.transmit(b'\xff')																								# Prepare device to receive instruction
        self.transmit(b'\x20')																								# Send rollUp code (0b00100000)
        self.transmit(b'\x70')

    def rollDown(self):
        self.transmit(b'\xff')																								# Prepare device to receive instruction
        self.transmit(b'\x30')																								# Send rollDown code (0b00110000)
        self.transmit(b'\x70')

    # GUI display code

    def getStatus(self):
        if self.status == 1:																								# If status of device = 1, then return Rolled Up
            return "Rolled up"
        elif self.status == 0:																								# If status of device = 0, then return Rolled Down
            return "Rolled down"

    # Setting code
    def setMinVal(self, minVal):
        self.minVal = minVal 																								# Change value of minVal to new user defined value
    # Add code to send this to Device 																					# Send new value to device

    def setRollPercentage(self, percentage):																				# Not working
        roll = percentage - self.rollPercentage 																			#
        self.transmit(roll)
        self.rollPercentage = percentage
