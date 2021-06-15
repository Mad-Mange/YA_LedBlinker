import serial
from time import sleep

ser = serial.Serial()
ser.baudrate = 2000000
ser.port = 'com3'
ser.open()

#"blink = 'led on\r\n'
blink = 'led blink\r\n'

ser.write(blink.encode('utf-8'))

sleep(10)

ser.close()