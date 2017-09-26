#!/usr/bin/env python3
from rplidar import RPLidar
import time

from settings import *

def run():
    lidar = RPLidar(PORT_NAME)
    time.sleep(WAIT)
    status, code = lidar.get_health()
    time.sleep(WAIT)
    lidar.disconnect()
    print(status)

if __name__ == '__main__':
    run()