#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.A)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=68, axle_track=180)

while True:
  threshold1 = line_sensor.reflection() - 25
  threshold2 = threshold1*-0.6
  robot.drive(-100, -threshold2)
