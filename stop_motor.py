#!/usr/bin/env python3
from rplidar import RPLidar

PORT_NAME = 'COM3'

def run():
    lidar = RPLidar(PORT_NAME)
    lidar.stop_motor()
    lidar.disconnect()

if __name__ == '__main__':
    run()