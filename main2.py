#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#initialize the ev3 brick
ev3 = EV3Brick()
 
#initialize the motors at port A and D
motorR = Motor(Port.A)
motorL = Motor(Port.D)

#initialize a ultrasonic sensor at port 1
eyes = UltrasonicSensor(Port.S1)


#Function creation 
def motorStop():
    motorR.run(0)
    motorL.run(0)
    

def motorFoward():
    motorR.run(1000)
    motorL.run(1000)
    

def motorBack():
    motorR.run(-1000)
    motorL.run(-1000)
    

def motorTurnRight():
    motorR.run(700)
    wait(500)
    motorL.run(1000)


def motorTurnLeft():
    motorL.run(700)
    wait(500)
    motorR.run(1000)


def motorSpin():
    motorR.run(400)
    motorL.run(-400)


search = False

while True:
    #check ultrassonic sensor distance
    a = eyes.distance()
    #the principal while
    while search == False:
        
        b = ev3brick.buttons()
        if Button.UP in b:
            motorFoward()
            wait(3000)
            motorStop()

        elif Button.DOWN in b:
            motorBack()
            wait(3000)
            motorStop()

        elif Button.RIGHT in b:
            motorTurnRight()
            wait(1000)
            motorFoward()
            wait(3000)
            motorStop()

        elif Button.LEFT in b:
            motorTurnLeft()
            wait(1000)
            motorFoward()
            wait(3000)
            motorStop()
    
        elif Button.CENTER in b:
            search = True
          
    #No colision
    while search == True:
        a = eyes.distance()
        print(a)
        if a <= 400:
            motorSpin()
    
        else:
            motorFoward()
        
        if Button.UP in b:
            motorStop()
            search = False
            
