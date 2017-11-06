import serial
import time

class Device():
	def __init__ (self, name, port, sensorType, rollDown):
		self.name = name
		self.port = port
		self.sensorType = sensorType
		self.status = 1 # 1 = rolled in, 0 = rolled out
		if rollDown != 0:
			self.rolldown = rollDown
		elif self.sensorType == "Light":
			self.rolldown = 50
		elif self.sensorType == "Temp":
			self.rolldown == 22
		self.establisch_connection()

	def set_rolldown(self, val):
		self.rolldown = val

	def establisch_connection(self):
		self.ser = serial.Serial(self.port, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

	# Roll down shutter (Only available in manual mode)
	def roll_down(self):
		self.ser.write(b'\xff') # Add to code to trigger function on arduino
		self.ser.write(b'\x30')

	# Roll up shutter (Only available in manual mode)
	def roll_up(self):
		self.ser.write(b'\xff') # Add to code to trigger function on arduino
		self.ser.write(b'\x20')

	def get_status(self):
		if self.status == 1:
			return "Rolled in"
		else:
			return "Rolled out"

	def transmit(self, message):
		self.ser.write(message)

	def receive(self):
		transmission = int('{:08b}'.format(ord(self.ser.read())),2)

		if transmission != 0xff:
			return

		self.transmit(b'\b01100000')

		value = 0
		print('Original value:', transmission)
		
		while True:
			transmission = int('{:08b}'.format(ord(self.ser.read())),2)
			self.transmit(b'\b01100000')
			print('Code: ', transmission)

			if transmission == 0b01000000:
				while True:
					transmission = int('{:08b}'.format(ord(self.ser.read())),2)
					self.transmit(b'\b01100000')
					print('Value: ', transmission)

					if transmission == 0b01110000:
						break
					else:
						value += transmission
				value /= 10
				print('Calculated value: ', value)
				break
			elif transmission == 0b01010001:
				self.status = 1
				print('Status set to 1')
				break
			elif transmission == 0b01010000:
				self.status = 0
				print('Status set to 0')
				break
			

#Test code
try:
	shutter_1 = Device("Attic", "COM5", "Light", 0)		
	print("Connection established")
	while True:
		shutter_1.receive()
except:
	print("Error: No device connected to port")