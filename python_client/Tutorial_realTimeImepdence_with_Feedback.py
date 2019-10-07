# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:56:31 2019

@author: Mohammad Safeea

Test script of realtime impedance mode
plot joints torques feedback while controlling the robot

"""

from iiwaPy import iiwaPy
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time
import math

def updateArrays(x,y,n,x1,y1):
    temp=n-1
    for i in range(temp):
        y[i]=y[i+1]
        x[i]=x[i+1]
    x[temp]=x1
    y[temp]=y1

def updatePlot(line,fig,x,y):
    line.set_xdata(x)
    line.set_ydata(y)
    plt.axis([x[0],x[-1],-1,1])
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    
# n=50
# x = np.zeros(n)
# y = np.sin(x)

# plt.ion()

# fig = plt.figure()
# graph = fig.add_subplot(111)
# line1, = graph.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

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
    # Motion variables
    w=0.6 # Angular velocity of the sinusoidal motion
    theta=0 # Motion displacment from equilibrium 
    interval= 2*math.pi # interval of motion
    a=math.pi/6   # Amplitude of motion
    counter=0 # To count the number of iterations
    index=0 # Index of the joint
    jposVec=iiwa.getJointsPos()
    j0Pos=jposVec[index]
    # Define the load data
    weightOfTool=1.0 # 1 kg 
    cOMx=0.0
    cOMy=0.0
    cOMz=0.0
    # Define stifness data
    cStiness=900
    rStifness=80
    nStifness=50
    iiwa.realTime_startImpedanceJoints(weightOfTool,cOMx,cOMy,cOMz,cStiness,rStifness,nStifness)
    # some timing variables
    t0=time.time()
    t_0=time.time()
    while theta<interval:
        deltat=time.time()-t0
        theta=w*deltat
        jposVec[index]=j0Pos-a*(1-math.cos(theta))       
        if (time.time()-t_0)>0.002:
            taw=iiwa.sendJointsPositionsGetMTorque(jposVec)
            print(taw)
            #print(taw)
            #y1=taw[0]
            #x1=deltat
            #updateArrays(x,y,n,x1,y1)
            #updatePlot(line1,fig,x,y)
            t_0=time.time()
            counter=counter+1
            
            
    deltat= time.time()-t0;
    iiwa.realTime_stopDirectServoJoints()   
except:
    print('an error happened')
    
iiwa.close()
print('update freq')
print(counter/deltat)