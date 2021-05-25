import math # pour faire des calculs 
import xbox # pour la manette
import time # mettre des delais
import serial # liaison serie
import numpy as np

    
if __name__ == '__main__':
    joy = xbox.Joystick()
    
    arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    
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
        
        if(RB):
            arduino.write(str('RB\n'))
            
                
        if(LB):
            arduino.write(str('LB\n'))
                          
        
        if(Y):
            arduino.write(str('Y\n'))
        
        if(LT):
            arduino.write(str('L\n'))
            
        if(RT):
            arduino.write(str('R\n'))
        
        if(B):
            arduino.write(str('B\n'))
            
        if(Pad_U):
            #xi = 0
            #yi = 1
            #vitesse = (xi**2+yi**2)*255
            #angle = np.arctan2(yi,xi)
            #angle = angle*180/math.pi
            #v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            #v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            #v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            #arduino.write(str(('v'+str(v1)+'\n')))
            #arduino.write(str(('w'+str(v2)+'\n')))
            #arduino.write(str(('u'+str(v3)+'\n')))
            arduino.write("PU\n")
        
        if(Pad_D):
#             xi = 0
#             yi = -1
#             vitesse = (xi**2+yi**2)*255
#             angle = np.arctan2(yi,xi)
#             angle = angle*180/math.pi
#             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
#             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
#             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
#             arduino.write(str(('v'+str(v1)+'\n')))
#             arduino.write(str(('w'+str(v2)+'\n')))
#             arduino.write(str(('u'+str(v3)+'\n')))
            arduino.write("PD\n")
            
        if(Pad_L):
#             xi = -1
#             yi = 0
#             vitesse = (xi**2+yi**2)*255
#             angle = np.arctan2(yi,xi)
#             angle = angle*180/math.pi
#             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
#             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
#             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
#             arduino.write(str(('v'+str(v1)+'\n')))
#             arduino.write(str(('w'+str(v2)+'\n')))
#             arduino.write(str(('u'+str(v3)+'\n')))
            arduino.write("PL\n")
                
        if(Pad_R):
#             xi = 1
#             yi = 0
#             vitesse = (xi**2+yi**2)*255
#             angle = np.arctan2(yi,xi)
#             angle = angle*180/math.pi
#             v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
#             v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
#             v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
#             arduino.write(str(('v'+str(v1)+'\n')))
#             arduino.write(str(('w'+str(v2)+'\n')))
#             arduino.write(str(('u'+str(v3)+'\n')))
            arduino.write("PR\n")
            
        if(X):
            arduino.write(str('X\n'))

        xi = joy.leftX()
        yi = joy.leftY()
        
        if(A):
            vitesse = (xi**2+yi**2)*255
            angle = np.arctan2(yi,xi)
            angle = angle*180/math.pi
            v1= int(vitesse/(1.5)*np.sin(np.radians(angle-90)))
            v2= int(vitesse/(1.5)*np.sin(np.radians(angle+30)))
            v3= int(vitesse/(1.5)*np.sin(np.radians(angle+150)))
            arduino.write(str(('v'+str(v1)+'\n')))
            arduino.write(str(('w'+str(v2)+'\n')))
            arduino.write(str(('u'+str(v3)+'\n')))
                
        #except Exception :
        #     arduino.write(str('B\n'))
            
    joy.close()
    
