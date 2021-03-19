import cv2
import calibrate
import picamera
import time
import os
import numpy as np
from datetime import datetime
import RPi.GPIO


#parametres
printing = True
saving_txt = False
display = False


path = '/home/pi/dev/projet_pir/vision/out/test/'

now = datetime.now()
save_dir = path + now.strftime("%d_%m_%Y-%H-%M-%S")
try:
    os.mkdir(f'{save_dir}')
except:
    raise ValueError('Impossible de creer le dossier de sauvegarde')



trigger = False
camera = picamera.PiCamera()
camera.rotation = 180

while not trigger :
    print('-------------------------')
    for i in range(4):
        print(f'starting in {4-i}')  
        time.sleep(1)
 
    print('starting ...')


    camera.capture(f'{save_dir}/original.jpg')
    if printing:
        print('taking picture : done')
    #precise the aruco dictionnary that we're using

    arucoDict = arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)
    if printing:
        print('loading dict : done')
    #create basics aruco params
    arucoParams = cv2.aruco.DetectorParameters_create()

    #load camera coefficients
    mtx,dist =calibrate.load_coefficients('/home/pi/dev/projet_pir/vision/params/myCalibration.yml')
    if mtx is None or dist is None :
        raise ValueError('Les parametres de calibration n ont pas ete bien importes')
    if printing:
        print('loading coeff : done')

    #loads the image
    original_image = cv2.imread(f'{save_dir}/original.jpg')
    #original_image = cv2.imread('/home/pi/dev/projet_pir/vision/out/test/18_03_2021-00-28-48/original.jpg')
    if printing:
        print('loading image : done')


    #save a copy of original
    curent = 'original'
    if display :
        cv2.imshow(curent,original_image)
    cv2.imwrite(f'{save_dir}/original_copy.jpg',original_image)


    #converts to grayscale and save
    img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    curent = 'grayscale'
    if display :
        cv2.imshow(curent,img)
    cv2.imwrite(f'{save_dir}/{curent}.jpg',img)
    if printing:
        print('grayscale : done')


    #detection des markers
    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict,
        parameters=arucoParams,cameraMatrix=mtx , distCoeff=dist)
    if printing:
        if ids is not None:
            print(f'detecting markers : {len(ids)} markers detected')
            print(f'Markers detectes :' , np.transpose(ids)[0])
        else:
            print('aucun marker detecte')


    #drawing detected markers
    img = cv2.aruco.drawDetectedMarkers(img,corners,ids,borderColor=(255,0,0)) #affichage
    curent = 'detected'
    if display :
        cv2.imshow(curent,img)
    cv2.imwrite(f'{save_dir}/{curent}.jpg',img)
    if printing:
        print('drawing markers : done')
    
    if ids is None:
        print("Aucun marker detecte")
    elif len(ids) > 1:
        raise ValueError("Plus d'un marker detecte")



    #estimation des orientations/translations
    rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners,100, mtx, dist) 
    if printing:
        print('estimating pose : done')


    #drawing all axis

    try :
        for i in range(len(rvecs)):
            rvec,tvec,numero=rvecs[i],tvecs[i],ids[i]
            img = cv2.aruco.drawAxis(original_image,mtx,dist,rvec,tvec,100) #affichage
            img = cv2.undistort(original_image, mtx, dist)
            img = cv2.circle(original_image,(int(len(original_image[0])/2),int(len(original_image)/2)), 10, (0,0,255), -1)

        if printing:
            print('drawing Axis : done')
            x=tvecs[0][0][0]
            y=tvecs[0][0][1]
            z=tvecs[0][0][2]
            print('x = ',x)
            print('y = ',y)
            print('z = ',z)
            distance_mes = np.sqrt(x**2 + y**2)
            if distance_mes<10:
                trigger=True
                print('Distance acceptee')
            print(f'Distance mesuree :{round(distance_mes,1)}mm')
            if x>0:
                print("decaler le tag sur la gauche")
            else:
                print("decaler le tag sur la droite")
            if y>0:
                print("decaler le tag vers la haut")
            else: 
                print("decaler le tag vers le bas")
        curent = 'axis'
        if display :
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow(curent,original_image)
        cv2.imwrite(f'{save_dir}/{curent}.jpg',img)


    except :
        pass

    #saving in text file
    if saving_txt :
        with open(f'{save_dir}/resultats.csv',mode='w') as f :
            f.writelines(f"Resultats de la detection : {len(ids)} markers detectes\n")
            f.writelines("id, x, y, z\n")
            for i,id in enumerate(ids):
                f.writelines(f'{id[0]}, {tvecs[i][0][0]}, {tvecs[i][0][1]}, {tvecs[i][0][1]}\n')
            if printing :
                print(f'writing output in {f.name}')
