#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.A)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=68, axle_track=180)

BLACK = 50
WHITE = 50
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 2

while True:
    deviation = line_sensor.reflection() - threshold
    
    turn_rate = PROPORTIONAL_GAIN * deviation

    robot.drive(-DRIVE_SPEED, -turn_rate)

