import os
from numpy import min,array,logical_and,reshape
from math import floor
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
        self.i = 0

    def run(self):
        # Set up pygame and the display
        os.putenv('SDL_FBDEV', '/dev/fb1')


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
                    distance = (array(scan))[:,2]
                    if process_data(distance) :
                        counter += 1
                    else :
                        counter = 0
                    
                    if counter > 2 : #nombre de tours consecutif pour considerer qu'un obstacles est bien present
                        self.dangerProximite = True
                        self.i+=1
                        print(f"Obstacle detecte depuis le lidar {self.i}")

            except adafruit_rplidar.RPLidarException as e:
                lidar.stop_motor()
                lidar.stop()
                lidar.disconnect()
                lidar = RPLidar(None, PORT_NAME)
                print('erreur de demarrage')

        lidar.stop_motor()
        lidar.stop()
        lidar.disconnect()



def process_data(data):
    trigger = False 
    if min(data)<300:
        trigger=True
            
    return trigger