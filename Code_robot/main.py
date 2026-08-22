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

leg_left = Motor(Port.C)
leg_right = Motor(Port.B)
back_left = Motor(Port.D)
back_right = Motor(Port.A)

gyro = GyroSensor(Port.S4)


# Variables

SPEED_LEG = 500      # °/s
SPEED_BACK = 300

LEG_ANGLE = 90       # Extension des jambes
BACK_ANGLE = 15      # Inclinaison du dos

TIME_IN_TOTAL = 60   # en millisecondes

# Position d'extension

def extend():

   # Jambes
    leg_left.run_target(SPEED_LEG, -LEG_ANGLE, wait=False)
    leg_right.run_target(SPEED_LEG, -LEG_ANGLE, wait=False)

    wait(1000)

    leg_left.hold()
    leg_right.hold()

    wait(100)

    
def retract():

    # Jambes
    leg_left.run_target(SPEED_LEG, 0, wait=False)
    leg_right.run_target(SPEED_LEG, 0, wait=False)

    wait(1000)

    leg_left.hold()
    leg_right.hold()

    wait(100)
 

def reset_all_angles():

    # Moteurs 
    leg_left.reset_angle(0)
    leg_right.reset_angle(0)
    back_left.reset_angle(0)
    back_right.reset_angle(0)


reset_all_angles()
gyro.reset_angle(0)

while True:

    speed_robot = gyro.speed()
    angle_robot = gyro.angle()

    ev3.screen.clear()
    ev3.screen.print("vitesse :", speed_robot)
    ev3.screen.print("angle :", angle_robot)
    



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

