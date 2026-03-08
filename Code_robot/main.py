#!/usr/bin/env pybricks-micropython 
# eh bah le robot a pas de pybricks installé

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)      
distance_sensor = UltrasonicSensor(Port.S4)

# Write your program here.

# Avancer
left_motor.run(300)      
right_motor.run(300)
wait(3000)               
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)