# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:56:31 2019

@author: Mohammad Safeea

Test PTP motion class
"""

from sunrisePy import sunrisePy
import time
import math
# Connect to the robot
ip='172.31.1.147'
#ip='localhost'
iiwa=sunrisePy(ip)
iiwa.setBlueOn()
time.sleep(2)
iiwa.setBlueOff()   

# read some data from the robot
try:
    # Move to an initial position
    jPos=[0,0,0,-math.pi/2,0,math.pi/2,0];
    print("Moving the robot in joint space to angular position")
    print(jPos)
    vRel=[0.1]
    print("With a relative velocity")
    print(vRel[0])
    iiwa.movePTPJointSpace(jPos,vRel)
    # Get current cartezian position
    print("Current Cartesian pose is")
    cPos=iiwa.getEEFPos()
    print(cPos)
    time.sleep(0.2)
    # Move ptp along x axis
    print('Moving on a line along the X axis')
    vel=[30]; # mm/sec
    print('With a linear velocity')
    print(vel)
    cPos[0]=cPos[0]+30
    iiwa.movePTPLineEEF(cPos,vel)
    # pause some time
    time.sleep(0.1)
    # Move ptp along z axis
    print('Moving on a line along the Z axis')
    vel=[10]; # mm/sec
    print('With a linear velocity')
    print(vel)
    cPos[2]=cPos[2]-50
    iiwa.movePTPLineEEF(cPos,vel)
except:
    print('an error happened')
    
iiwa.close()