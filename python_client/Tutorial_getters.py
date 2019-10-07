# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:03:26 2018

@author: Mohammad SAFEEA

Test script of iiwaPy class.

"""
from iiwaPy import iiwaPy
import time
ip='172.31.1.147'
#ip='localhost'
iiwa=iiwaPy(ip)
iiwa.setBlueOn()
time.sleep(2)
iiwa.setBlueOff()
# read some data from the robot
try:
    print('End effector position and orientation is:')
    print(iiwa.getEEFPos())
    time.sleep(0.1)
    print('Forces acting at end effector are')
    print(iiwa.getEEF_Force())
    time.sleep(0.1)
    print('Cartezian position (X,Y,Z) of end effector')
    print(iiwa.getEEFCartizianPosition())
    time.sleep(0.1)
    print('Moment at end effector')
    print(iiwa.getEEF_Moment())
    time.sleep(0.1)
    print('Joints positions')
    print(iiwa.getJointsPos())
    time.sleep(0.1)
    print('External torques at the joitns')
    print(iiwa.getJointsExternalTorques())
    time.sleep(0.1)
    print('Measured torques at the joints')
    print(iiwa.getJointsMeasuredTorques())
    time.sleep(0.1)
    print('Measured torque at joint 5')
    print(iiwa.getMeasuredTorqueAtJoint(5))
    time.sleep(0.1)
    print('Rotation of EEF, fixed rotation angles (X,Y,Z)')
    print(iiwa.getEEFCartizianOrientation())
    time.sleep(0.1)
    
    print('Joints positions has been streamed external torques are:')
    print(iiwa.getEEFCartizianOrientation())
    time.sleep(0.1)
    
except:
    print('an error happened')
    
iiwa.close()

