#!/usr/bin/env python3
from rplidar import RPLidar

from settings import PORT_NAME

def run():
    lidar = RPLidar(PORT_NAME)
    lidar.stop_motor()
    lidar.disconnect()

if __name__ == '__main__':
    run()