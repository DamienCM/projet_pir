import math # pour faire des calculs 
import xbox # pour la manette
import time # mettre des delais
import serial # liaison serie
import numpy as np

    
if __name__ == '__main__':
    joy = xbox.Joystick()
    
    # arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    
    while not joy.Back():
        # try:
        
        time.sleep(0.1)
        
        A = joy.A()
        B = joy.B()
        X = joy.X()
        Y = joy.Y()
        
        RT = joy.rightTrigger() > 0.8
        RB = joy.rightBumper()
        LT = joy.leftTrigger() > 0.8
        LB = joy.leftBumper()
        S = joy.Start()

        Pad_U = joy.dpadUp()
        Pad_D = joy.dpadDown()
        Pad_L = joy.dpadLeft()
        Pad_R = joy.dpadRight()
        
        if(LT):
            # print(str('L\n'))
            print("L")
            
        if(RT):
            # print(str('R\n'))
            print("R")
        
        if(B):
            # print(str('B\n'))
            print("B")
            
        if(Pad_U):
            xi = 0
            yi = 1
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
        
        if(Pad_D):
            xi = 0
            yi = -1
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
            
        if(Pad_L):
            xi = -1
            yi = 0
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
                
        if(Pad_R):
            xi = 1
            yi = 0
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
            
        if(X):
            print(str('X\n'))

        xi = joy.leftX()
        yi = joy.leftY()
        if(A):
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
                
        #except Exception :
        #     print(str('B\n'))
            
    joy.close()
    
