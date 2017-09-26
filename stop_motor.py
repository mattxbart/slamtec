#!/usr/bin/env python3
from rplidar import RPLidar
import time
from settings import *

def run():
    lidar = RPLidar(PORT_NAME)
    time.sleep(WAIT)
    lidar.stop_motor()
    time.sleep(WAIT)
    lidar.disconnect()

if __name__ == '__main__':
    run()