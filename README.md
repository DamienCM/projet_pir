# Projet d'intégration robotique FULL OPEN SOURCE
## Encadré par M. MOSSER Loic
### Réalisation d'un robot holonome avec de nombreuses fonctionnalités

![alt text](https://puu.sh/HqlWj/9c79ee2674.png)

----
# Cahier des charges synthetique:
1. Contrôle par mannette de Xbox
2. Contrôle par coordonnees programmees
3. Contrôle par vision grâce à des tags aRuco
----
# Fonctionnement du repertoire

Pour utiliser le repertoire correctement il est nécessaire de placer le repertoire en local sur la pi a l'emplacement suivant :
***/home/pi/dev/projet_pir/***

Le projet se decompose en plusieurs sous repertoires : 
* CAO (non présente sur le repertoire)
* Asservissement des moteurs ***projet_pir/asserv***
* Contrôle des autres actionneurs (buzzer et servo)  ***projet_pir/actionneurs***
* Algorithme de vision OpenCV ***projetr_pir/vision***
* Utilisation d'un Lidar permettant d'arrêter le robot en cas de proximité d'un obstacle ***projet_pir/lidar***

----

# Vision
La vision se décompose autour de plusieurs scripts python :
1. Un algorithme permettant de calibrer la camera ***calibration.py*** (essentiel avant toute autre etape). Celui ci sauvegarde les resultats dans le fichier ***params/myCalibration.yml***
2. Un algorithme de calcul d'angle de la camera ***calcul_angle.py***. Il permet de calculer l'inclinaison autour de l'axe horizonal, il est necessaire de faire cela car les coordonees renvoyees sont prises dans le referentiel de la camera ie z normal au PCB de la camera. C'est essentiel afin de pouvoir transferer ces corrdonnees dans le repere du robot. Cet angle est sauvegarde dans un fichier texte present dans */params/angle_camera.txt*
3. Un/des algorithme.s permettant d'identifier les tags et de renvoyer leur position relative du robot dans la sortie standart ou dans un fichier texte. Il y a un ***vision.py***  permettant d'etre execute en rentrant les parametres dans le fichier, et un autre ****vision_inline.py*** qui permet de rentrer les arguments de maniere standart dans le shell : 
>pi@rasberrypi: ~/dev/projet_pir $ sudo python3 vision_inline.py arg1 arg2 arg3
4. Un script tres simple ***camera.py*** permettant de prendre une photo
5. Un autre script simple permettant de generer des tags aRuco depuis les dictionnaire et de les sauvegarder aau format .pdf

----

# Asservissement



----

# Actionneurs
todo

----

# Lidar
todo

----



PS : RIP in peace LabVIEW
