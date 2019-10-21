# -*- coding: utf-8 -*-
"""
Created on Tue Oct  21 17:56:31 2019

@author: Mohammad Safeea

Test PTP motion class with costum TCP tranform
"""

from iiwaPy import iiwaPy
import time
import math
# Connect to the robot
ip='172.31.1.147'
# The following is the transform of TCP with respect to the flange of the robot
TPCtransform=(50,25,0,0,0,0) #(x,y,z,alfa,beta,gama)
iiwa=iiwaPy(ip,TPCtransform)
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
    # Testing PTP line relative motions
    jPos=[0,math.pi*20/180,0,-math.pi*70/180,0,math.pi*60/180,0];
    vRel=[0.1]
    iiwa.movePTPJointSpace(jPos,vRel)
    # Print current Cartesian position
    print('Current Cartesian position')
    print(iiwa.getEEFPos())
    # Line motion of EEF (specified relatively in base frame) 
    deltaX=0
    deltaY=0
    deltaZ=100 # (mm)
    vel=[150] #(mm/sec)
    pos=[deltaX,deltaY,deltaZ]
    print('Performing Linear motion relatively defined in Base-frame')
    iiwa.movePTPLineEefRelBase(pos,vel)
    pos[2]=-deltaZ
    iiwa.movePTPLineEefRelBase(pos,vel)
    # Line motion of EEF (specified relatively in EEF frame)
    print('Performing Linear motion relatively defined in EEF-frame')
    pos[2]=deltaZ
    iiwa.movePTPLineEefRelEef(pos,vel)
    pos[2]=-deltaZ
    iiwa.movePTPLineEefRelEef(pos,vel)
    # Performing Arc motion
    # Move to an initial position
    print('Moving on Arcs')
    print('First going to some initial configuration')
    jPos=[0,-math.pi*10/180,0,-math.pi*100/180,math.pi*90/180,math.pi/2,0];
    print("Moving the robot in joint space to angular position")
    print(jPos)
    vRel=[0.1]
    print("With a relative velocity")
    print(vRel[0])
    iiwa.movePTPJointSpace(jPos,vRel)
    # Get current position of EEF
    print('Current Cartesian Pose')
    f1=iiwa.getEEFPos()
    print(f1)
    f2=list(f1)
    r=75
    f1[1]=f1[1]+r
    f1[2]=f1[2]-r
    f1[5]=f1[5]+math.pi/8
    f2[2]=f2[2]-2*r
    f2[5]=f2[5] + math.pi/2
    vel = [50]
    iiwa.movePTPCirc1OrintationInter(f1,f2,vel)
    # Move in joint space to another initial configuration
    jPos=[0,math.pi*20/180,0,-math.pi*70/180,0,math.pi*90/180,0]
    relVel=[0.15]
    iiwa.movePTPJointSpace(jPos,relVel)
    # Move EEF -100 mm in z direction
    Pos=[0.0,0.0,-100.0]
    vel = [50]
    iiwa.movePTPLineEefRelBase(Pos,vel)
    # Consider current position as the center of the arc
    cen=iiwa.getEEFPos()
    # Move EEF 50mm in X direction
    Pos=[50.0,0.0,0.0]
    iiwa.movePTPLineEefRelBase(Pos,vel)
    # Store current Cartesian position in memory
    begginingPoint=iiwa.getEEFPos()
    # Moving in an arc, the arc is in an incliend plane
    theta=[math.pi/2]
    k=[1,1,1]
    vel=[100]
    c=[cen[0],cen[1],cen[2]]
    print('Moving on an incliend Arc')
    iiwa.movePTPArc_AC(theta,c,k,vel)
    # Go back to beggining point
    vel=[150] # velocity mm/sec
    iiwa.movePTPLineEEF(begginingPoint,vel)
    # Move on an Arc in the XY plange
    # using functiom movePTPArcXY_AC
    theta=[1.98*math.pi]
    c=[cen[0],cen[1]]
    vel=[150]
    print('Moving on an incliend Arc parallel to XY plane')
    iiwa.movePTPArcXY_AC(theta,c,vel)
    
except:
    print('an error happened')
    
iiwa.close()