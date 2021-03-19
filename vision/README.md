# Remarque importante a propos des reperes

OpenCV ne peut nous donner que les coordonnees des markers par rapport au repere de la camera. Nous devons les adapter afin qu'elles concordent avec celles du robot.

![alt text](https://puu.sh/HqyII/a762954c54.png)

Ainsi en mesurant L et H on peut faire la conversion car on connaitra **gamma**. Pour mesurer L et H correctement il faut utiliser le script **orientation.py** pour faire concorder l'axe z de la camera avec un tag au sol.

Une fois L et H mesures (en mm) il faut les rentrer dans le fichier **/vision/params/angle_camera.csv**. Il faut aussi rentrer dx (en mm)

Il seront ensuite pris en compte dans le script principal de vision vision.py et vision_inline.py