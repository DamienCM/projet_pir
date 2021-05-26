import lidar.lidar_sans_affichage as lidar
#import vision.vision as vision
import asserv.test_manette as manette
import asserv.xbox
import time
#execute les donnees de vision
# os.system('sudo python  vision/vision_inline.py')




if __name__ == "__main__":
    print('debut')
    print('on unitialise lobjet lidar')
    lid = lidar.MyLidar()
    man=manette.Manette()
    print('on demmare le lidar')
    lid.start()
    man.start()
    print('on peut continuer le main')
    while True:
        time.sleep(.1)
        if lid.dangerProximite:
            # print("demande d'arret tansmise depuis le main")
            man.arret = False
        else:
            # print("demande de non arretet depuis le main ")
            man.arret = False

