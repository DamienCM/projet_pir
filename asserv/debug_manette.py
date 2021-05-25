import math # pour faire des calculs 
import xbox # pour la manette
import time # mettre des delais
import serial # liaison serie
import numpy as np



if __name__ == '__main__':
    joy = xbox.Joystick()
    
    
    # arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    
    while not joy.Back():
        
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
            # arduino.write(str('L\n'))
            print("L")
            
        if(RT):
            # arduino.write(str('R\n'))
            print("R")
        if(B):
            #arduino.write(str('B\n'))
            print("B")
        if(Pad_U):
            #arduino.write(str('PU\n'))
            print("Pad_U")
        if(Pad_D):
            #arduino.write(str('PD\n'))
            print("Pad_D")
        if(Pad_L):
            # arduino.write(str('PL\n'))
            print("Pad_L")
        if(Pad_R):
            # arduino.write(str('PR\n'))
            print("Pad_R")
        if(X):
            # arduino.write(str('X\n'))
            print("X")
#         if(A):
#             arduino.write(str('a'))
#           
#         if(B):
#             arduino.write(str('b'))
#             
#         if(X):
#             arduino.write(str('x'))
#             
#         if(Y):
#             arduino.write(str('y'))
#             
#         if(RT):
#             arduino.write(str('r\n'))
#             
#         if(LT):
#             arduino.write(str('l\n'))
#             
#         if(RB):
#             arduino.write(str('m'))
#             
#         if(LB):
#             arduino.write(str('n'))
        xi = joy.leftX()
        yi = joy.leftY()
        vitesse = (xi**2+yi**2)*255
        angle = np.arctan2(yi,xi)
        angle = angle*180/math.pi
        v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
        v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
        v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
        if(A):
            print(str(('v'+str(v1)+'\n')))
            print(str(('w'+str(v2)+'\n')))
            print(str(('u'+str(v3)+'\n')))
#         
       
    joy.close()
