import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
"""
On va generer les tags 6x6 cases avec 250mm de cote sous la forme d'un tableau suivant
0 1 2 3
4 5 6 7
8 9 10 11
"""

fig = plt.figure()
nx = 4
ny = 3
for i in range(0, nx*ny):
    ax = fig.add_subplot(ny,nx, i+1)
    img = aruco.drawMarker(aruco_dict,i, 700)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("out/aruco/markers.pdf")
plt.show()