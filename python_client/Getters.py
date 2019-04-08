# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:42:39 2018

@author: Mohammad SAFEEA
"""

from GeneralPurpose import getDoubleFromString

class Getters:
    
    def __init__(self,mysoc):
        self.mysoc=mysoc

    def send(self,data,size):
        data=data+'\n'
        self.mysoc.send(data)
        message=self.mysoc.receive()
        #print(message)
        #sys.stdout.flush()
        return getDoubleFromString(message,size)
        
    def sendShort(self,data):
        data=data+'\n'
        self.mysoc.send(data)
        message=self.mysoc.receive()
        return float(message)
       
# getters           
    def getEEFPos(self):
        theCommand='Eef_pos'
        eefPos=self.send(theCommand,6)
        return eefPos
        
    def getEEF_Force(self):
        theCommand='Eef_force'
        force=self.send(theCommand,3)
        return force
        
    def getEEFCartizianPosition(self):
        theCommand='Eef_pos'
        eefPos=self.send(theCommand,3)
        return eefPos
        
    def getEEF_Moment(self):
        theCommand='Eef_moment'
        moment=self.send(theCommand,3)
        return moment
        
    def getJointsPos(self):
        theCommand='getJointsPositions'
        jointsPos=self.send(theCommand,7)
        return jointsPos
        
    def getJointsExternalTorques(self):
        theCommand='Torques_ext_J'
        taw=self.send(theCommand,7)
        return taw
    
    def getJointsMeasuredTorques(self):
        theCommand='Torques_m_J'
        taw=self.send(theCommand,7)
        return taw
        
    def getMeasuredTorqueAtJoint(self,x):
        theCommand='Torques_m_J'
        taw=self.send(theCommand,7)
        return taw[x-1] # array index starts from zero, joint index start from one
    
    def getEEFCartizianOrientation(self):
        theCommand='Eef_pos'
        eefPos=self.send(theCommand,6)
        return eefPos[3:6]
        
        
# get pin states        
    def getPin3State(self):
        theCommand='getPin3'
        state=self.sendShort(theCommand)
        return state
        
    def getPin4State(self):
        theCommand='getPin4'
        state=self.sendShort(theCommand)
        return state
        
    def getPin10State(self):
        theCommand='getPin10'
        state=self.sendShort(theCommand)
        return state
        
    def getPin13State(self):
        theCommand='getPin13'
        state=self.sendShort(theCommand)
        return state
        
    def getPin16State(self):
        theCommand='getPin16'
        state=self.sendShort(theCommand)
        return state
    