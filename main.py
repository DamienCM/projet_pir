import lidar.lidar_inline
import threading


# try:
#     print('moteurs allumes')
#     main_lidar()
# except DangerProximite:
#     print('etteindre moteur DNA')






if __name__ == "__main__":
    print('debut')
    x = threading.Thread(target=lidar.lidar_inline.main)
    print('on commence le thread')
    x.start()
    print('on demaree le lidar')
    x .join()
    #ARRET MOTEURS

    #code qui ne marche pas
    # print('debut')
    # x = threading.Thread(target=lidar.lidar_inline.main)
    # print('on commence le thread')
    # try :
    #     x.start()
    #     print('on demaree le lidar')
    #     x .join()
    #     #ARRET MOTEURS
    # except Exeption presente dans le thread:
    #     doSomthing()