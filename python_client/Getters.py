# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:42:39 2018
Updated 1-Oct-2019
A while loop is added in the get functions. 
@author: Mohammad SAFEEA
"""

from GeneralPurpose import getDoubleFromString

class Getters:
    
    def __init__(self,mysoc):
        self.mysoc=mysoc
        self.numOfIterations=5

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
        eefPos=[]
        i=0
        while len(eefPos)==0: # Keeps trying (up-to numOfIterations) until data is read successfully
            theCommand='Eef_pos'
            eefPos=self.send(theCommand,6)
            i=i+1
            if i==self.numOfIterations:
                return eefPos # break
        return eefPos
        
    def getEEF_Force(self):
        force=[]
        i=0
        while len(force)==0: # Keeps trying (up-to numOfIterations) until data is read successfully
            theCommand='Eef_force'
            force=self.send(theCommand,3)
            i=i+1
            if i==self.numOfIterations:
                return force # return (breaks the loop)
        return force
        
    def getEEFCartizianPosition(self):
        eefPos=[]
        i=0
        while len(eefPos)==0:
            theCommand='Eef_pos'
            eefPos=self.send(theCommand,3)
            i=i+1
            if i==self.numOfIterations:
                return eefPos
        return eefPos
        
    def getEEF_Moment(self):
        moment=[]
        i=0
        while len(moment)==0:
            theCommand='Eef_moment'
            moment=self.send(theCommand,3)
            i=i+1
            if i==self.numOfIterations:
                return moment
        return moment
        
    def getJointsPos(self):
        jointsPos=[]
        i=0
        while len(jointsPos)==0:
            theCommand='getJointsPositions'
            jointsPos=self.send(theCommand,7)
            i=i+1
            if i==self.numOfIterations:
                return jointPos
        return jointsPos
        
    def getJointsExternalTorques(self):
        taw=[]
        i=0
        while len(taw)==0:
            theCommand='Torques_ext_J'
            taw=self.send(theCommand,7)
            i=i+1
            if i==self.numOfIterations:
                return taw
        return taw
    
    def getJointsMeasuredTorques(self):
        taw=[]
        i=0
        while len(taw)==0:
            theCommand='Torques_m_J'
            taw=self.send(theCommand,7)
            i=i+1
            if i==self.numOfIterations:
                return taw            
        return taw
        
    def getMeasuredTorqueAtJoint(self,x):
        r=x-int(x)
        if (x<1) or (x>7) or (not(r*r==0)):
            print("Joint index shall be an integer from 1 to 7")
        taw=[]
        i=0
        while len(taw)==0:
            theCommand='Torques_m_J'
            taw=self.send(theCommand,7)
            i=i+1
            if i==self.numOfIterations:
                return taw[x-1]
        return taw[x-1] # array index starts from zero, joint index start from one
    
    def getEEFCartizianOrientation(self):
        eefPos=[]
        i=0
        while len(eefPos)==0:
            theCommand='Eef_pos'
            eefPos=self.send(theCommand,6)
            i=i+1
            if i==self.numOfIterations:
                return eefPos[3:6]       
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