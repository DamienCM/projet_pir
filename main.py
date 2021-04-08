import lidar.lidar_inline as lidar
import vision.vision as vision

#execute les donnees de vision
# os.system('sudo python  vision/vision_inline.py')




if __name__ == "__main__":
    print('debut')
    print('on unitialise lobjet lidar')
    lid = lidar.MyLidar()
    print('on demmare le lidar')
    lid.start()
    print('on peut continuer le main')
