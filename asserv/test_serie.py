import serial
import time

arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

while(True):
    arduino.write(str('a'))
    time.sleep(.1)