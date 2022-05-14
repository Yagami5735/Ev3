#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 brick.
ev3 = EV3Brick()


# Initialize a motor at port B.
motor = Motor(Port.B)
# Play a sound.

sensor = ColorSensor(Port.S1)

eyes = UltrasonicSensor(Port.S2)

gyro = GyroSensor(Port.S3)

while True:
    
    a = sensor.color()
    b = sensor.reflection()
    c = gyro.angle()
    d = eyes.distance()
    print(a)
    print(b)
    print(c)
    if (b <= 40 and b != 0):
        
        motor.run(1000)
        if(c >= 10):
            motor.reset_angle(0)
            motor.dc(c + 30)
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
        #    motor.run(0)a
        

    else:


        motor.run(0)


        