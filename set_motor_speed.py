#!/usr/bin/env python3
from rplidar import RPLidar
import sys
import time
from settings import PORT_NAME

def run(MOTOR_PWM):
    lidar = RPLidar(PORT_NAME)
    time.sleep(1)
    lidar._motor_speed = MOTOR_PWM
    lidar.start_motor()
    time.sleep(1)
    lidar.disconnect()

if __name__ == '__main__':
    run(int(sys.argv[1]))