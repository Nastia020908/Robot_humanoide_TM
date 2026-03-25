#!/usr/bin/env pybricks-micropython 
# eh bah le robot a pas de pybricks installé

from pybricks.hub import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)      
distance_sensor = UltrasonicSensor(Port.S4)

# Write your program here.

# le beep pour tester
ev3.speaker.beep()

# Boucle principale
while True:
    
    distance = distance_sensor.distance()

    if distance < 200:  # obstacle à moins de 20 cm
        left_motor.stop(Stop.BRAKE)
        right_motor.stop(Stop.BRAKE)
        ev3.speaker.beep()
        break
    
    else:
        left_motor.run(300)
        right_motor.run(300)

    wait(100)