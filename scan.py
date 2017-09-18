#!/usr/bin/env python3
import sys
import numpy as np
from rplidar import RPLidar
import time
from settings import PORT_NAME
import os

def run(DURATION, FILENAME):
    lidar = RPLidar(PORT_NAME)
    time.sleep(.5)
    timeout = time.time() + DURATION  # in seconds
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
    data = open(FILENAME, 'ab')
    while True:
        t = 0
        count = 0
        for scan in lidar.iter_scans():
            count += 1
            np.savetxt(data, np.array(scan))
            if t == DURATION or time.time() > timeout:
                break
            t = t - 1

        break
    lidar.disconnect()
    #print statement required to capture value for vba shell
    print(count)


if __name__ == '__main__':
    run(int(sys.argv[1]), sys.argv[2])