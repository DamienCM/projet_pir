import RPi.GPIO as GPIO
import math
import xbox
import numpy as np
import serial,time
 
GPIO_LED_GREEN  = 23
GPIO_LED_RED    = 22
GPIO_LED_YELLOW = 27
GPIO_LED_BLUE   = 17
 
GPIO_SERVO_PIN  = 25
 
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(GPIO_LED_GREEN, GPIO.OUT)
GPIO.setup(GPIO_LED_RED, GPIO.OUT)
GPIO.setup(GPIO_LED_YELLOW, GPIO.OUT)
GPIO.setup(GPIO_LED_BLUE, GPIO.OUT)
GPIO.setup(GPIO_SERVO_PIN, GPIO.OUT)
 
 
def updateServo(pwm, angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
 
def angleFromCoords(x,y):
    angle = 0.0
    if x==0.0 and y==0.0:
        angle = 90.0
    elif x>=0.0 and y>=0.0:
        # first quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else 90.0
    elif x<0.0 and y>=0.0:
        # second quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x<0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x>=0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else -90.0
        angle += 360.0
    return angle
 
if __name__ == '__main__':
    joy = xbox.Joystick()
    pwm = GPIO.PWM(GPIO_SERVO_PIN, 100)
    pwm.start(5)
    
    while not joy.Back():
        xi = joy.leftX()
        yi = joy.leftY()
        # LEDs
        led_state_green  = GPIO.HIGH if xi < 0 else GPIO.LOW
        led_state_red    = GPIO.HIGH if xi > 0 else GPIO.LOW
        led_state_yellow = GPIO.HIGH if yi < 0 else GPIO.LOW
        led_state_blue   = GPIO.HIGH if yi > 0 else GPIO.LOW
            
        GPIO.output(GPIO_LED_GREEN, led_state_green)
        GPIO.output(GPIO_LED_RED, led_state_red)
        GPIO.output(GPIO_LED_YELLOW, led_state_yellow)
        GPIO.output(GPIO_LED_BLUE, led_state_blue)
        
        vitesse = (xi**2+yi**2)*100
        angle = np.arctan2(yi,xi)
        angle = angle*180/math.pi
        
        print("vitesse = ", vitesse)
        print("angle = ", angle)
#         venc="V"+vitesse
#         Anglenc = "A"+angle
        
   
    
    joy.close()
    pwm.stop()
# if __name__=='__main__':
#     print('Running. Press CTRL-C to exit.')
#     with serial.Serial("/dev/nom_port", 9600, timeout=1) as arduino :
#         time.sleep(0.1)
#         if arduino.isOpen():
#             print("{} is connected!".format(arduino.port))
#             try:
#                 while True:
#                     print(venc.format(arduino.port))
#                     print(Anglenc.format(arduino.port))
#                     
#                     while arduino.inWaiting()==0 : pass
#                     if arduino.inWaiting()>0:
#                         answer=arduino.readline()
#                         print(answer)
#             except KeyboardInterrupt :
#                 print("KeyboardInterrupt has been caught.")