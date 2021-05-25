import math # pour faire des calculs 
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
            # print(f'manette arret {self.arret}')
            if self.arret:
                print("demande d'arret transmise")
                while True:
                    self.arduino.write(str.encode(('B\n')))
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
                
                    
            if(LB):
                self.arduino.write(str.encode(('LB\n')))
                            
            
            if(Y):
                self.arduino.write(str.encode(('Y\n')))
            
            if(LT):
                self.arduino.write(str.encode(('L\n')))
                
            if(RT):
                self.arduino.write(str.encode(('R\n')))
            
            if(B):
                self.arduino.write(str.encode(('B\n')))
                
            if(Pad_U):
                #xi = 0
                #yi = 1
                #vitesse = (xi**2+yi**2)*255
                #angle = np.arctan2(yi,xi)
                #angle = angle*180/math.pi
                #v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
                #v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
                #v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
                #self.arduino.write(str.encode((('v'+str.encode((v1)+'\n')))
                #self.arduino.write(str.encode((('w'+str.encode((v2)+'\n')))
                #self.arduino.write(str.encode((('u'+str.encode((v3)+'\n')))
                self.arduino.write("PU\n")
            
            if(Pad_D):
    #             xi = 0
    #             yi = -1
    #             vitesse = (xi**2+yi**2)*255
    #             angle = np.arctan2(yi,xi)
    #             angle = angle*180/math.pi
    #             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
    #             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
    #             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
    #             self.arduino.write(str.encode((('v'+str.encode((v1)+'\n')))
    #             self.arduino.write(str.encode((('w'+str.encode((v2)+'\n')))
    #             self.arduino.write(str.encode((('u'+str.encode((v3)+'\n')))
                self.arduino.write("PD\n")
                
            if(Pad_L):
    #             xi = -1
    #             yi = 0
    #             vitesse = (xi**2+yi**2)*255
    #             angle = np.arctan2(yi,xi)
    #             angle = angle*180/math.pi
    #             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
    #             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
    #             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
    #             self.arduino.write(str.encode((('v'+str.encode((v1)+'\n')))
    #             self.arduino.write(str.encode((('w'+str.encode((v2)+'\n')))
    #             self.arduino.write(str.encode((('u'+str.encode((v3)+'\n')))
                self.arduino.write("PL\n")
                    
            if(Pad_R):
    #             xi = 1
    #             yi = 0
    #             vitesse = (xi**2+yi**2)*255
    #             angle = np.arctan2(yi,xi)
    #             angle = angle*180/math.pi
    #             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
    #             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
    #             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
    #             self.arduino.write(str.encode((('v'+str.encode((v1)+'\n')))
    #             self.arduino.write(str.encode((('w'+str.encode((v2)+'\n')))
    #             self.arduino.write(str.encode((('u'+str.encode((v3)+'\n')))
                self.arduino.write("PR\n")
                
            if(X):
                self.arduino.write(str.encode(('X\n')))

            xi = self.joy.leftX()
            yi = self.joy.leftY()
            
            if(A):
                vitesse = (xi**2+yi**2)*255
                angle = np.arctan2(yi,xi)
                angle = angle*180/math.pi
                v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
                v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
                v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
                self.arduino.write(str.encode((('v'+str(v1)+'\n'))))
                self.arduino.write(str.encode((('w'+str(v2)+'\n'))))
                self.arduino.write(str.encode((('u'+str(v3)+'\n'))))
                print('A')
                    
            #except Exception :
            #     self.arduino.write(str('B\n'))
            

        self.joy.close()
    
