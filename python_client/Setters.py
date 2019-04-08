# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:42:39 2018

@author: Mohammad SAFEEA
"""

import sys

class Setters:
    
    def __init__(self,mysoc):
        self.mysoc=mysoc

    def send(self,data):
        data=data+'\n'
        self.mysoc.send(data)
        message=self.mysoc.receive()
        print(message)
        sys.stdout.flush()
        
    def setBlueOff(self):
        theCommand='blueOff'
        self.send(theCommand)
        
    def setBlueOn(self):
        theCommand='blueOn'
        self.send(theCommand)
        
    def setPin1Off(self):
        theCommand='pin1off'
        self.send(theCommand)
        
    def setPin1On(self):
        theCommand='pin1on'
        self.send(theCommand)
        
    def setPin2Off(self):
        theCommand='pin2off'
        self.send(theCommand)
        
    def setPin2On(self):
        theCommand='pin2on'
        self.send(theCommand)
        
    def setPin11Off(self):
        theCommand='pin11off'
        self.send(theCommand)
        
    def setPin11On(self):
        theCommand='pin11on'
        self.send(theCommand)
        
    def setPin12Off(self):
        theCommand='pin12off'
        self.send(theCommand)
        
    def setPin12On(self):
        theCommand='pin12on'
        self.send(theCommand)
        
        