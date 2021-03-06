#!/usr/bin/env python3
import sys
import numpy as np
from rplidar import RPLidar
import time
from settings import PORT_NAME

def run():
    lidar = RPLidar(PORT_NAME)
    lidar.reset()
    #print statement required to capture value for vba shell
    print("reset sent")
    time.sleep(.1)
    lidar.disconnect()


if __name__ == '__main__':
    run()