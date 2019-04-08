# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:08:12 2018

@author: Mohammad SAFEEA

Example for controlling iiwa using GUI from an external PC
"""

from Tkinter import *
from sunrisePy import sunrisePy

class App:
    def __init__(self):
        root = Tk()
        self.IP_of_robot= StringVar()
        self.stateMessage=StringVar()
        self.jText=[0 for x in xrange(7)]
        
            
        root.title('Control iiwa remotly from external PC')
        upperFrame=Frame(root)
        upperFrame.pack()
        
        buttonHeight=2
        buttonWidth=12
        
        Label(upperFrame, text="Joint").grid(row=0)
        Label(upperFrame, text="Angle").grid(row=0, column=1)
        """
        
        e1 = Entry(upperFrame)
        e2 = Entry(upperFrame)
        
        e1.grid(row=1, column=0)
        e2.grid(row=1, column=1)
        """
        
        j=0
        for i in range(7):
            j=j+1
            labelName="J"+str(j)
            Label(upperFrame, text=labelName).grid(row=j, column=0)
            self.jText[i]=StringVar()
            self.jText[i].set("0.0")
            Entry(upperFrame,justify='center',textvariable=self.jText[i]).grid(row=j, column=1)
        
            if i==0:
                Label(upperFrame, text="    IP:").grid(row=j+1, column=3) 
                IPtxt=Entry(upperFrame,textvariable=self.IP_of_robot).grid(row=j+1, column=4)
                self.IP_of_robot.set("172.31.1.147")
            elif i==1:
                Label(upperFrame, text=" State:").grid(row=j+1, column=3) 
                IPtxt=Entry(upperFrame,textvariable=self.stateMessage).grid(row=j+1, column=4)
                self.stateMessage.set("Not connected")
            else:
                Label(upperFrame, text="      ").grid(row=j+1, column=3)   
        
        """The following is a space holder"""
        Label(upperFrame, text="    ").grid(row=j+1, column=0) 
        """ScrolledText(upperFrame).grid(columnspan=2)"""
        rowNum=1  
        Button(upperFrame,text="Connect",fg="red", command=self.connectFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=4)
        Button(upperFrame,text="turn off server",fg="red", command=self.disconnectFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="add new point",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="delete last point",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="perform program",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="advance one step",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="Go home",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(upperFrame,text="About",fg="red", height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        
        
        S = Scrollbar(root)
        T = Text(root, height=4, width=50)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        root.mainloop()
        
    def connectFun(self):
        message="Connecting to robot at ip: "+self.IP_of_robot.get()
        self.printMessage(message)
        self.iiwa=sunrisePy(self.IP_of_robot.get())
        jpos=self.iiwa.getJointsPos()
        for i in range(7):
            self.jText[i].set(str(jpos[i] ))       
            print "value of joint "+str(i)
            print self.jText[i].get()
            
    def disconnectFun(self):
        message="Disconnecting from robot"
        print message
        self.iiwa.close()
        
    def printMessage(self,message):
        print message
        self.stateMessage.set(message)
             


Appliaction=App()
 




