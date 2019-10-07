# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:56:31 2019

@author: Mohammad Safeea

Test script of realtime impedance mode
plot joints torques feedback while controlling the robot

"""

from iiwaPy import iiwaPy
from datetime import datetime
import time
import math

def getSecs():
    t = datetime.now()
    sec = ((t.day * 24 +t.hour)* 60 + t.minute)*60 + t.second  + t.microsecond / 1000000.0
    return sec

# Connect to the robot
ip='172.31.1.147'
#ip='localhost'
iiwa=iiwaPy(ip)
iiwa.setBlueOn()
time.sleep(2)
iiwa.setBlueOff()   

# read some data from the robot
try:
    # Move to an initial position    
    jPos=[0,0,0,-math.pi/2,0,math.pi/2,0];
    vRel=[0.1]
    iiwa.movePTPJointSpace(jPos,vRel)

    # define some variables:
    counter=0 # count the number of iterations
    index=0 # index (the first joint angle)
    w=0.6 # angular velocity of the motion
    theta=0 # angular command for the first joint
    interval= 4*math.pi # 2*pi
    a=math.pi/6 # amplitude of the motion
    # Read current joints positions
    jpos=iiwa.getJointsPos()
    jpos0_6=jpos[index]
    print("Currnet joints positions")
    print(jpos)
    # Define the load data
    weightOfTool=1.0 # 1 kg 
    cOMx=0.0
    cOMy=0.0
    cOMz=0.0
    
    cStiness=900
    rStifness=80
    nStifness=50
    
    iiwa.realTime_startImpedanceJoints(weightOfTool,cOMx,cOMy,cOMz,cStiness,rStifness,nStifness)
    iiwa.realTime_stopDirectServoJoints()
    
    iiwa.realTime_startImpedanceJoints(weightOfTool,cOMx,cOMy,cOMz,cStiness,rStifness,nStifness)
    
    t0=getSecs()
    t_0=getSecs()
    while theta<interval:
        theta=w*(getSecs()-t0)
        jpos[index]=jpos0_6+a*math.sin(theta)
        
        if (getSecs()-t_0)>0.002:
            iiwa.sendJointsPositions(jpos)
            t_0=getSecs()
            counter=counter+1
            
            
    deltat= getSecs()-t0;
    # movig point to point again
    print('Turning off realtime control')
    iiwa.realTime_stopDirectServoJoints()
    print('Realtime control turned off')
    time.sleep(0.5)
    jPos=[0,0,0,-math.pi/2,0,math.pi/2,0];
    print('Moving in joint space to position')
    print(jPos)
    vRel=[0.1]
    iiwa.movePTPJointSpace(jPos,vRel)
    
except:
    print('an error happened')
    
iiwa.close()
print('Socket update freq for the ServoMotion')
print(counter/deltat)