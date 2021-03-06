import os
from math import cos, sin, pi, floor
import pygame
import adafruit_rplidar
from adafruit_rplidar import RPLidar
import IPython
from threading import Thread


class DangerProximite(Exception):
    pass

class MyLidar(Thread):
    def __init__(self):
        super(MyLidar, self).__init__()
        self.dangerProximite = False

    def run(self):
        # Set up pygame and the display
        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()
        lcd = pygame.display.set_mode((320,240))
        pygame.mouse.set_visible(False)
        lcd.fill((0,0,0))
        pygame.display.update()

        # Setup the RPLidar
        PORT_NAME = '/dev/ttyUSB0'
        lidar = RPLidar(None, PORT_NAME)

        # used to scale data to fit on the screen
        max_distance = 0

        #pylint: disable=redefined-outer-name,global-statement

        scan_data = [0]*360

        while True:
            try:
                #print(lidar.info)
                counter = 0
                for scan in lidar.iter_scans():

                    for (_, angle, distance) in scan:
                        scan_data[min([359, floor(angle)])] = distance
                    if process_data(scan_data,lcd,max_distance) :
                        counter += 1
                    else :
                        counter = 0
                    
                    if counter > 10 :
                        self.dangerProximite = True
                        print()

            except adafruit_rplidar.RPLidarException as e:
                lidar.stop_motor()
                lidar.stop()
                lidar.disconnect()
                lidar = RPLidar(None, PORT_NAME)
                print('erreur de demarrage')

        lidar.stop_motor()
        lidar.stop()
        lidar.disconnect()



def process_data(data,lcd,max_distance):
    lcd.fill((0,0,0)) 
    trigger = False    
    for angle in range(360):
        distance = data[angle]
        if distance > 0:   
            if distance < 200:               #penser a remettre 500 # ignore initially ungathered data points
                # print(f'Distance = {distance}')
                # print ("Objet detecte")
                trigger =True
            max_distance = max([min([5000, distance]), max_distance])
            radians = angle * pi / 180.0
            x = distance * cos(radians)
            y = distance * sin(radians)
            point = (160 + int(x / max_distance * 119), 120 + int(y / max_distance * 119))
            lcd.set_at(point, pygame.Color(255, 255, 255))
    pygame.display.update()
    return trigger