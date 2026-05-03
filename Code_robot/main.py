#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S4)      
distance_sensor = UltrasonicSensor(Port.S1)
touch_sensor = TouchSensor(Port.S3)
gyro = GyroSensor(Port.S2)

# Write your program here.


# le beep pour tester
# ev3.speaker.beep()


# test 1: detection d'obstacle + arret

#while True:
    #distance = distance_sensor.distance()

    #if distance < 100:  # à moins de 10 cm
        #left_motor.stop(Stop.BRAKE)
        #right_motor.stop(Stop.BRAKE)
        #ev3.speaker.beep()
        #break
    #else:
        #left_motor.run(400)
        #right_motor.run(400)

    #wait(100)


# test 2: detection de couleur bleue + arret

#while True:
    #color = color_sensor.color()

    #if color == "BLUE":
        #left_motor.stop(Stop.BRAKE)
        #right_motor.stop(Stop.BRAKE)
        #ev3.speaker.beep()
        #break

    #else:
        #left_motor.run(400)
        #right_motor.run(400)

    #wait(100)


# test 3: bouton préssé + arret

#while True:
    #if touch_sensor.pressed():
        #left_motor.stop(Stop.BRAKE)
        #right_motor.stop(Stop.BRAKE)
        #break
    #else:
        #left_motor.run(400)
        #right_motor.run(400)

    #wait(100)

# test 4: gyrosensor -> marche pas, le sensor est pas connecté

#gyro.reset_angle()
#wait(500)

# rotation du robot (sur place)
#left_motor.run(200)
#right_motor.run(-200)

# on laisse tourner un moment
#wait(2000)

# arrêt des moteurs
#left_motor.stop()
#right_motor.stop()

# lecture de l'angle final
#angle = gyro.angle()

# affichage sur écran EV3
#from pybricks.hubs import EV3Brick
#ev3 = EV3Brick()

#ev3.screen.clear()
#ev3.screen.print("Angle final:", angle)