import serial
import time


def print_status(msg):
	print('=> Debug: {0}'.format(msg))


class Device():
	def __init__(self, name, portNumber, sensorType, minVal, maxLength):
		self.name = name        																							# Custom name of device. For example: Living room
		self.status = 1																										# 1 = rolled up, 0 = rolled down
		self.portNumber = portNumber																						# Port used to connect to device
		self.sensorType = sensorType																						# Type of sensor used in device
		self.maxLength = maxLength																							# Maximun roll distance of the shutter
		self.rollPercentage = 0																								# Percentage shutter has rolled out. Between 0 and 100

		if minVal != 0:																										# If custom value is given use that value
			self.minVal = minVal		
		elif self.sensorType == "Light":																					# If no custom value is given and sensor type = "Light" use default light value
			self.minVal = 50
		elif self.sensorType == "Temp":																						# If no custom value is given and sensor type = "Temp" use default light value
			self.minVal = 22

		self.establishConnection()																							# Establish connection using given port
		time.sleep(2)																										# Wait to finish establishing connection

		self.transmit(0xff)																									# Start maxLength transmission
		self.transmit(0b00010001)																							# Send code to set maxLength
		self.transmit(int(10.0 * self.maxLength))																			# Send maxLength value
		self.transmit(0b01110000)																							# End data transmission

		time.sleep(1)																										# Pause between transmission

		self.transmit(0xff)																									# Start minVal transmission
		self.transmit(0b00010010)																							# Send code to set minVal
		value = int(10 * self.minVal)																						# Turn float into integer
		while True:
			if (value - 255) > 0:																							# If value is larger than 8 bits send 255
				self.transmit(255)
				value -= 255																								# Subtract 255 from value
			else:																											# Else send value
				self.transmit(value)
				break																				
		self.transmit(0b01110000)																							# End data transmission

	# Connection code
	def establishConnection(self):
		self.connection = serial.Serial(self.portNumber, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE) 	# Opens port to device.

	def transmit(self, message):
		self.connection.write(bytes([message]))																				# Send message to device, Can use decimal, binary

	def receive(self):
		data = self.connection.read()

		if not data:
			return

		transmission = int(ord(data))
		value = 0

		if transmission != 0xff:
			return

		while True:
			data = self.connection.read()
			transmission = int(ord(data))

			if transmission == 0b01000000:
				while True:
					data = self.connection.read()
					transmission = int(ord(data))

					if transmission == 0b01110000:
						break
					else:
						value += transmission

				value /= 10
				print(value)
				break
			elif transmission == 0b01010001:
				print("Shutter rolled up")
				self.status = 1
				break
			elif transmission == 0b01010000:
				print("Shutter rolled down")
				self.status = 0
				break
	#OBSOLETE
	def rollUp(self):
		self.transmit(0xff)																									# Prepare device to receive instruction
		self.transmit(0x20)																									# Send rollUp code (0b00100000)
		self.transmit(0b01110000)																							# End data transmission

	#OBSOLETE
	def rollDown(self):
		self.transmit(0xff)																									# Prepare device to receive instruction
		self.transmit(0x30)																									# Send rollDown code (0b00110000)
		self.transmit(0b01110000)																							# End data transmission

	# GUI display code
	def getName(self):
		return self.getName 																								# Returns name of a device

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
		self.transmit(0xff)
		self.transmit(0b00100000)
		self.transmit(percentage)
		self.rollPercentage = percentage

# Test code
port = 'COM5'

try:
	shutter = Device("Attic", port, "Light", 10, 0.10)
	print("Connection established on {0}".format(port))
#
#	counter = 0
	
	i = 1

	while True:
#		#print_status('Sending empty transmission to Arduino')
		shutter.transmit(1)
#
#		#print_status('begin transmission cycle: {0}'.format(counter))
		shutter.receive()
		#if i == 1:
		#	time.sleep(10)
		#	shutter.rollDown()
		#	i = 2
#		#shutter.transmit(64)
#		#print_status('end')
#
#		#counter += 1
#
#	#time.sleep(5)
#	#shutter.transmit(0xff)
#	#print("Rolling down")
except Exception as e:
	print(e)