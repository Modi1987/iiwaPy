# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:03:26 2018

@author: Mohammad SAFEEA

Test script of iiwaPy class.

"""
from sunrisePy import sunrisePy
import math
import time
from datetime import datetime

start_time = datetime.now()
# returns the elapsed seconds since the start of the program
def getSecs():
    dt = datetime.now() - start_time
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) + dt.microseconds / 1000000.0
    return ms


ip = "172.31.1.147"
# ip='localhost'
iiwa = sunrisePy(ip)
iiwa.setBlueOn()
time.sleep(2)
iiwa.setBlueOff()
# read some data from the robot
try:
    counter = 0
    index = 0
    w = 0.6 * 3
    theta = 0
    interval = 2 * 3.14
    a = 3.14 / 6

    jpos = iiwa.getJointsPos()
    jpos0_6 = jpos[index]
    iiwa.realTime_startDirectServoJoints()

    t0 = getSecs()
    t_0 = getSecs()
    while theta < interval:
        theta = w * (getSecs() - t0)
        jpos[index] = jpos0_6 - a * (1 - math.cos(theta))

        if (getSecs() - t_0) > 0.002:
            iiwa.sendJointsPositions(jpos)
            t_0 = getSecs()
            counter = counter + 1

    deltat = getSecs() - t0
    iiwa.realTime_stopDirectServoJoints()

except:
    print("an error happened")

iiwa.close()
print("update freq")
print(counter / deltat)
