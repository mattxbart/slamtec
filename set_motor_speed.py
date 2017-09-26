#!/usr/bin/env python3
from rplidar import RPLidar
import sys
import time
from settings import *

def run(MOTOR_PWM):
    lidar = RPLidar(PORT_NAME)
    time.sleep(WAIT)
    lidar.reset()
    time.sleep(WAIT)
    lidar._motor_speed = MOTOR_PWM
    lidar.start_motor()
    time.sleep(WAIT)
    lidar.disconnect()

if __name__ == '__main__':
    run(int(sys.argv[1]))