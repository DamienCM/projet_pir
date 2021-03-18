# Projet d'integration robotique
## Encadre par M. MOSSER Loic
### Realisation d'un robot holonome avec de nombreuses fonctionnalites
----
# Cahier des charges synthetique:
1. Controle par mannette de Xbox
2. Controle par coordonnees programmees
3. Controle par vision grace a des tags aRuco
----
# Fonctionnement du repertoire

Pour utiliser le repertoire correctement il est necessaire de placer le repertoire en local sur la pi a l'emplacement suivant :
***/home/pi/dev/projet_pir/***

Le projet se decompose en plusieurs sous repertoires : 
* CAO (non presente sur le repertoire)
* Asservissement des moteurs ***projet_pir/asserv***
* Controle des autres actionneurs (buzzer et servo)  ***projet_pir/actionneurs***
* Algorithme de vision OpenCV ***projetr_pir/vision***
* Utilisation d'un Lidar permettant d'arreter le robot en cas de proximite d'un obstacle ***projet_pir/lidar***

----

# Vision
La vision se decompose autour de plusieurs scripts python :
1. Un algorithme permettant de calibrer la camera ***calibration.py*** (essentiel avant toute autre etape). Celui ci sauvegarde les resultats dans le fichier ***params/myCalibration.yml***
2. Un algorithme de calcul d'angle de la camera ***calcul_angle.py***. Il permet de calculer l'inclinaison autour de l'axe horizonal, il est necessaire de faire cela car les coordonees renvoyees sont prises dans le referentiel de la camera ie z normal au PCB de la camera. C'est essentiel afin de pouvoir transferer ces corrdonnees dans le repere du robot. Cet angle est sauvegarde dans un fichier texte present dans */params/angle_camera.txt*
3. Un/des algorithme.s permettant d'identifier les tags et de renvoyer leur position relative du robot dans la sortie standart ou dans un fichier texte. Il y a un ***vision.py***  permettant d'etre execute en rentrant les parametres dans le fichier, et un autre ****vision_inline.py*** qui permet de rentrer les arguments de maniere standart dans le shell : 
>pi@rasberrypi: ~/dev/projet_pir $ sudo python3 vision_inline.py arg1 arg2 arg3
4. Un script tres simple ***camera.py*** permettant de prendre une photo
