#!/usr/bin/env python3
import sys
import numpy as np
from rplidar import RPLidar
import time
PORT_NAME = 'COM3'

def run(DURATION):
    lidar = RPLidar(PORT_NAME)
    lidar.reset()
    timeout = time.time() + DURATION  # in seconds
    print('Recording measurments...')

    data = open(r'C:\Users\mbartolome\PycharmProjects\slamtec\scan.txt', 'ab')
    while True:
        test = 0
        for scan in lidar.iter_scans():
            np.savetxt(data, np.array(scan))
            if test == 5 or time.time() > timeout:
                break
            test = test - 1
        break
    lidar.disconnect()


if __name__ == '__main__':
    run(int(sys.argv[1]))