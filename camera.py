from picamera import PiCamera
import calibrate
import time


camera = PiCamera()
camera.rotation = 180
camera.capture('out/camera/test_aruco.jpg')
