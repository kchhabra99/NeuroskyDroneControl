import os
from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 
while ser.in_waiting==True:
	ser.readline()
while True:
	x=ser.readline()
	x.strip() 	
	print int(x) 
 
