        while True:
            try:
                #print(lidar.info)
                counter = 0
                for scan in lidar.iter_scans():

                    for (_, angle, distance) in scan:
                        scan_data[min([359, floor(angle)])] = distance
                    if process_data(scan_data,lcd,max_distance) :
                        counter += 1
                    else :
                        counter = 0
                    
                    if counter > 10 :
                        self.dangerProximite = True

            except adafruit_rplidar.RPLidarException as e:
                lidar.stop_motor()
                lidar.stop()
                lidar.disconnect()
                lidar = RPLidar(None, PORT_NAME)
                print('erreur de demarrage')