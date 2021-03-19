import cv2
import calibrate
import picamera
import time
import os
import numpy as np
from datetime import datetime
import sys,getopt

#parametres
printing = True # as -p
saving_txt = True #as -s
display = False #as -d
delay = False #as -t tempo

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"p:s:d:t:")
for o, a in myopts:
    if o == '-p':
        printing=bool(a)
    elif o == '-s':
        saving_txt=bool(a)
    elif o == '-d':
        display=bool(a)
    elif o == '-t':
        delay=bool(a)
    else:
        raise ValueError(f"Usage: -d display -s saving -t tempo -p printing \nInput argument error unknown : {o}")


#dossier de sauvegarde
path = '/home/pi/dev/projet_pir/vision/out/test/' 
now = datetime.now()
save_dir = path + now.strftime("%d_%m_%Y-%H-%M-%S")


#temporisation
if delay  :
    for i in range(4):
        print(f'starting in {4-i}')   
        time.sleep(1)
    print('starting ...')
try:
    os.mkdir(f'{save_dir}')
except:
    raise ValueError('Impossible de creer le dossier de sauvegarde')


#prise de photo
# camera = picamera.PiCamera()
# camera.rotation = 180
# camera.capture('{save_dir}/test_aruco.jpg')
if printing:
    print('taking picture : done')


#precise the aruco dictionnary that we're using
arucoDict = arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
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
#original_image = cv2.imread('{save_dir}/test_aruco.jpg')
original_image = cv2.imread('/home/pi/dev/projet_pir/vision/out/test/16_03_2021-19-07-58/original.jpg')
if printing:
    print('loading image : done')


#save a copy of original
curent = 'original'
if display :
    cv2.imshow(curent,original_image)
cv2.imwrite(f'{save_dir}/original.jpg',original_image)


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
    print(f'detecting markers : {len(ids)} markers detected')
    if ids is not None:
        print(f'Markers detectes :' , np.transpose(ids)[0])


#drawing detected markers
img = cv2.aruco.drawDetectedMarkers(img,corners,ids,borderColor=(255,0,0)) #affichage
curent = 'detected'
if display :
    cv2.imshow(curent,img)
cv2.imwrite(f'{save_dir}/{curent}.jpg',img)
if printing:
    print('drawing markers : done')


#estimation des orientations/translations
rvecs, tvecs, _objPoints = cv2.aruco.estimatePoseSingleMarkers(corners,25, mtx, dist) 
if printing:
    print('estimating pose : done')


#drawing all axis
try :
    for i in range(len(rvecs)):
        rvec,tvec,numero=rvecs[i],tvecs[i],ids[i]
        img = cv2.aruco.drawAxis(original_image,mtx,dist,rvec,tvec,100) #affichage
    if printing:
        print('drawing Axis : done')
    curent = 'axis'
    if display :
        cv2.imshow(curent,original_image)
    cv2.imwrite(f'{save_dir}/{curent}.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
