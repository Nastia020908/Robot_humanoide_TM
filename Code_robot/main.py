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

leg_left = Motor(Port.A)
leg_right = Motor(Port.B)
back_left = Motor(Port.C)
back_right = Motor(Port.D)

gyro = GyroSensor(Port.S2)


# Variables

SPEED_LEG = 300      # °/s
SPEED_BACK = 300

LEG_ANGLE = 90       # Extension des jambes
BACK_ANGLE = 60      # Inclinaison du dos

TIME_IN_TOTAL = 60

# Position d'extension

def extend():

    # Jambes
    leg_left.run_target(SPEED_LEG, LEG_ANGLE, wait=False)
    leg_right.run_target(SPEED_LEG, LEG_ANGLE, wait=False)

    # Dos 
    back_left.run_target(SPEED_BACK, 0, wait=False)
    back_right.run_target(SPEED_BACK, 0, wait=True)

# Retour en boule

def retract():

    # Jambes
    leg_left.run_target(SPEED_LEG, 0, wait=False)
    leg_right.run_target(SPEED_LEG, 0, wait=False)

    # Dos
    back_left.run_target(SPEED_BACK, BACK_ANGLE, wait=False)
    back_right.run_target(SPEED_BACK, -BACK_ANGLE, wait=True)

# Write your program here.

# Remettre le capteur à 0
gyro.reset_angle()

# Impulsion initiale
extend()
wait(500)
retract()
wait(500)

# Chrono
timer = StopWatch()

while timer.time() < TIME_IN_TOTAL * 1000:

    speed_robot = gyro.speed()
    angle_robot = gyro.angle()

    if abs(speed_robot) < 10 and angle_robot > 0:
    # Point extrême avant
    retract()

    elif abs(speed_robot) < 10 and angle_robot < 0:
    # Point extrême arrière
    extend()

    else:
    # Rien faire
    pass

    


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
    #ev3.screen.clear()
    #ev3.screen.print("Couleur détectée", color)

    #if color == Color.BLUE:        
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

# affichage sur écran EV3, sert a rien on a deja tout
#from pybricks.hubs import EV3Brick
#ev3 = EV3Brick()

#ev3.screen.clear()
#ev3.screen.print("Angle final:", angle)

