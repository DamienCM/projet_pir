import math

from numpy.testing._private.utils import print_assert_equal # pour faire des calculs 
import asserv.xbox as xbox# pour la manette
import time # mettre des delais
import serial # liaison serie
import numpy as np
from threading import Thread
    
class Manette(Thread):
    def __init__(self):
        super(Manette, self).__init__()
        self.arret = False
        self.joy = xbox.Joystick()
        self.arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    
    def run(self):
        while not self.joy.Back():
            # try:
            time.sleep(.1)
            print(f'manette arrete ? {self.arret}')
            if self.arret:
                
                while True:
                    print(f'manette arrete ? {self.arret}')
                    self.arduino.write(str.encode(('B\n')))
                    if not self.arret :
                        break
            time.sleep(0.1)
            
            A = self.joy.A()
            B = self.joy.B()
            X = self.joy.X()
            Y = self.joy.Y()
            
            RT = self.joy.rightTrigger() > 0.8
            RB = self.joy.rightBumper()
            LT = self.joy.leftTrigger() > 0.8
            LB = self.joy.leftBumper()
            S = self.joy.Start()

            Pad_U = self.joy.dpadUp()
            Pad_D = self.joy.dpadDown()
            Pad_L = self.joy.dpadLeft()
            Pad_R = self.joy.dpadRight()
            
            if(RB):
                self.arduino.write(str.encode(('RB\n')))
                print('RB')
                
                    
            if(LB):
                self.arduino.write(str.encode(('LB\n')))
                print('LB')            
            
            if(Y):
                self.arduino.write(str.encode(('Y\n')))
                print('Y')
            if(LT):
                self.arduino.write(str.encode(('L\n')))
                print('L')
            if(RT):
                self.arduino.write(str.encode(('R\n')))
                print('R')
            if(B):
                self.arduino.write(str.encode(('B\n')))
                print('B')
            if(Pad_U):
                print('PU')
                self.arduino.write(str.encode("PU\n"))
            
            if(Pad_D):
                print('PD')
                self.arduino.write(str.encode("PD\n"))
                
            if(Pad_L):
                print('PL')
                self.arduino.write(str.encode("PL\n"))
                    
            if(Pad_R):
                self.arduino.write(str.encode("PR\n"))
                print('PR')
            if(X):
                self.arduino.write(str.encode(('X\n')))
                print('X')
            xi = self.joy.leftX()
            yi = self.joy.leftY()
            
            if(A):
                vitesse = (xi**2+yi**2)*255
                angle = np.arctan2(yi,xi)
                angle = angle*180/math.pi
                v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
                
                v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
                v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
                print(v1,v2,v3)
                self.arduino.write(str.encode((('v'+str(v1)+'\n'))))
                self.arduino.write(str.encode((('w'+str(v2)+'\n'))))
                self.arduino.write(str.encode((('u'+str(v3)+'\n'))))
                print('A')
                    
            #except Exception :
            #     self.arduino.write(str('B\n'))
            

        self.joy.close()
    
