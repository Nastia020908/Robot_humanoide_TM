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

leg_left = Motor(Port.D)
leg_right = Motor(Port.A)
back_left = Motor(Port.C)
back_right = Motor(Port.B)

gyro_right = GyroSensor(Port.S2)
gyro_left = GyroSensor(Port.S3)

# Variables

SPEED_LEG = 400      # °/s
SPEED_BACK = 200

LEG_ANGLE = 90       # Extension des jambes
BACK_ANGLE = 60      # Inclinaison du dos

ZERO_GAP = 2
NOT_ZERO_GAP = 10

# Fonctions

def extend():

    back_left.run_target(SPEED_BACK, 0, wait=False)
    back_right.run_target(SPEED_BACK, 0, wait=True)
    leg_left.run_target(SPEED_LEG, -LEG_ANGLE, wait=False)
    leg_right.run_target(SPEED_LEG, -LEG_ANGLE, wait=True)
    

    wait(1000)

    leg_left.hold()
    leg_right.hold()
    back_left.hold()
    back_right.hold()

    wait(1000)

    
def retract():

    back_left.run_target(SPEED_LEG, -BACK_ANGLE, wait=False)
    back_right.run_target(SPEED_LEG, -BACK_ANGLE, wait=False)
    leg_left.run_target(SPEED_LEG, 0, wait=False)
    leg_right.run_target(SPEED_LEG, 0, wait=True)
    
    wait(1000)

    leg_left.hold()
    leg_right.hold()
    back_left.hold()
    back_right.hold()

    wait(1000)
 

def reset_all_angles():

    leg_left.reset_angle(0)
    leg_right.reset_angle(0)
    back_left.reset_angle(0)
    back_right.reset_angle(0)


def check_gyros(): 

    gyro_left.reset_angle(0)

    while True:

        speed_robot = gyro_right.speed()
        angle_robot = gyro_left.angle()

        ev3.screen.clear()
        ev3.screen.print("vitesse :", speed_robot)
        ev3.screen.print("angle :", angle_robot)
    
def extend_retract():

    back_left.run_target(SPEED_BACK, 0, wait=False)
    back_right.run_target(SPEED_BACK, 0, wait=True)
    leg_left.run_target(SPEED_LEG, -LEG_ANGLE, wait=False)
    leg_right.run_target(SPEED_LEG, -LEG_ANGLE, wait=True)
    
    wait(1000)

    back_left.run_target(SPEED_LEG, -BACK_ANGLE, wait=False)
    back_right.run_target(SPEED_LEG, -BACK_ANGLE, wait=False)
    leg_left.run_target(SPEED_LEG, 0, wait=False)
    leg_right.run_target(SPEED_LEG, 0, wait=True)

    wait(1000)

def extend_retract_test():

    extend_retract()
    extend_retract()
    extend_retract()
    extend_retract()

def changing_signs():

    previous_speed = 0

    while True:

        speed = gyro_right.speed()

        if previous_speed > 0 and speed < 0:
            extend()

        elif previous_speed < 0 and speed > 0:
            retract()

        previous_speed = speed


def balance_at_0():

    while True:

        speed = gyro_right.speed()
    
        if abs(speed) < 3:
            extend_retract()


def spot_turning_points():

    action_running = False

    while True:

        speed_robot = gyro_right.speed()
        angle_robot = gyro_left.angle()

        if abs(speed_robot) < ZERO_GAP and not action_running:

            if angle_robot > 0:
                extend()
                action_running = True

            elif angle_robot < 0:
                retract()
                action_running = True

        elif abs(speed_robot) > NOT_ZERO_GAP:
            action_running = False

        else:
            pass

        wait(10)

def spot_turning_points_upgraded():

    action_running = False
    was_moving = False

    while True:

        speed_robot = gyro_right.speed()
        angle_robot = gyro_left.angle()

        if abs(speed_robot) > NOT_ZERO_GAP:
            was_moving = True
            action_running = False

        elif abs(speed_robot) < ZERO_GAP and was_moving and not action_running:

            if angle_robot > 0:
                extend()
                action_running = True

            elif angle_robot < 0:
                retract()
                action_running = True

            was_moving = False

        wait(10)

def test_gyros_list():

    gyro_right.reset_angle(0)
    gyro_left.reset_angle(0)

    speed_values = []
    angle_values = []

    for i in range(500):

        speed_robot = gyro_right.speed()
        angle_robot = gyro_left.angle()

        speed_values.append(speed_robot)
        angle_values.append(angle_robot)

        wait(10)

    print("SPEED")
    for value in speed_values:
        print(value)

    print("ANGLE")
    for value in angle_values:
        print(value)

def beep_at_turning_point():

    beeped = False

    while True:

        speed_robot = gyro_right.speed()

        if abs(speed_robot) < ZERO_GAP and not beeped:
            ev3.speaker.beep()
            beeped = True

        if abs(speed_robot) > NOT_ZERO_GAP:
            beeped = False

        wait(10)


beep_at_turning_point()




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

