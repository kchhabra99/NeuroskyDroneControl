import serial
ser = serial.Serial('/dev/ttyACM0',57600)

while ser.in_waiting== True:
	ser.readline()
	x.strip()
	print int(x)

