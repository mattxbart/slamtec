#!/usr/bin/env python3
from rplidar import RPLidar
import sys

PORT_NAME = 'COM3'

def run(MOTOR_PWM):
    lidar = RPLidar(PORT_NAME)
    lidar._motor_speed = MOTOR_PWM
    lidar.start_motor()
    lidar.disconnect()

if __name__ == '__main__':
    run(int(sys.argv[1]))