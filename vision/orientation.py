import cv2
import calibrate
import picamera
import time
import os
from datetime import datetime



while True :
    display = True
    delay = False

    now = datetime.now()
    save_dir = now.strftime("%d_%m_%Y-%H-%M-%S")

    if delay  :
        for i in range(4):
            time.sleep(1)
            print(i)   


    os.mkdir(f'/home/pi/Desktop/S8/PIR/out/angle/{save_dir}/')

    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.capture('/home/pi/Desktop/S8/PIR/out/angle/test_aruco.jpg')

    #precise the aruco dictionnary that we're using
    arucoDict = arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)

    #create basics aruco params
    arucoParams = cv2.aruco.DetectorParameters_create()

    #load camera coefficients
    mtx,dist =calibrate.load_coefficients('params/calibration.yml')

    #loads the image
    original_image = cv2.imread('/home/pi/Desktop/S8/PIR/out/angle/test_aruco.jpg')


    #save a copy of original
    curent = 'original'
    if display :
        cv2.imshow(curent,original_image)
    cv2.imwrite(f'/home/pi/Desktop/S8/PIR/out/angle/{save_dir}/original.jpg',original_image)

    #converts to grayscale and save
    img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    curent = 'grayscale'
    if display :
        cv2.imshow(curent,img)
    cv2.imwrite(f'out/test/{save_dir}/{curent}.jpg',img)


    #detection des markers
    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict,
        parameters=arucoParams,cameraMatrix=mtx , distCoeff=dist)

    # print(f'Corners = {corners}')
    # print(f'ids = {ids}')
    # print(f'rejected = {rejected}')

    img = cv2.aruco.drawDetectedMarkers(img,corners,ids,borderColor=(255,0,0)) #affichage
    curent = 'detected'
    if display :
        cv2.imshow(curent,img)
    cv2.imwrite(f'/home/pi/Desktop/S8/PIR/out/angle/{save_dir}/{curent}.jpg',img)



    #estimation des orientations/translations
    rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners,100, mtx, dist) 
    try :
        for i in range(len(rvecs)):
            rvec,tvec,numero=rvecs[i],tvecs[i],ids[i]
            print(f'tvec={tvec}',f'numero={numero}')
            img = cv2.aruco.drawAxis(original_image,mtx,dist,rvec,tvec,100) #affichage

        curent = 'axis'
        if display :
            cv2.imshow(curent,original_image)
        cv2.imwrite(f'/home/pi/Desktop/S8/PIR/out/angle/{save_dir}/{curent}.jpg',img)
        cv2.waitKey(10)
        cv2.destroyAllWindows()

    except :
        pass

    print(f'Tags aruco detecte : {ids}')
