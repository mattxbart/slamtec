#!/usr/bin/env python3
from rplidar import RPLidar
import time

PORT_NAME = 'COM3'

def run():
    lidar = RPLidar(PORT_NAME)
    time.sleep(.5)
    status, code = lidar.get_health()
    lidar.disconnect()
    print(status)

if __name__ == '__main__':
    run()