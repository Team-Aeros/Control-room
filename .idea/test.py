import serial
import time

ser = serial.Serial("COM5", 19200)
time.sleep(5)
ser.write(00000001)