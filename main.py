#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Seta o EV3Brick
ev3 = EV3Brick()

#Seta a porta B para o motor
motor = Motor(Port.B)

#Seta a porta 1 para o sensor de cor
sensor = ColorSensor(Port.S1) 

#Seta a porta 2 para o sensor ultrasonico
eyes = UltrasonicSensor(Port.S2)

while True:
    
    a = sensor.color()      #Le o que está sendo detectado no sensor de cor
    b = sensor.reflection() #Le o que está sendo detectado no sensor de refletancia
    c = eyes.distance()     #Le o que está sendo detectado no sensor ultrasonico
    print(a)
    print(b)
    print(c)
    if (b >= 60):
        
        motor.run(1000) #motor anda com toda a potencia
        #b = ev3brick.buttons()
        #if Button.LEFT in b:
        #    ev3.speaker.beep()

        #    motor.run(1000)
        #    wait(2000)
        #
        #    motor.run(0)
        #elif Button.RIGHT in b:
        #    ev3.speaker.beep(1000, 500)
        #    motor.run(-1000)
        #    wait(2000)
        #    motor.run(0)
    elif(c < 100):

        
        motor.run(1000)

    else:

        
        motor.run(0) #motor para de rodar

        
