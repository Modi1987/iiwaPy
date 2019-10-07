# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:08:12 2018
Updated 2019-Oct-07

@author: Mohammad SAFEEA

Example for controlling iiwa using GUI from an external PC
"""

from Tkinter import *
from iiwaPy import iiwaPy
import math

class App:
    def __init__(self):
        root = Tk()
        self.root=root
        self.IP_of_robot= StringVar()
        self.stateMessage=StringVar()
        self.connection_state=False
        self.jText=[0 for x in xrange(7)]
        self.commandsList=[]
        self.commandsAngleList=[]
            
        root.title('Control iiwa remotly from external PC')
        mainFrame=Frame(root)
        mainFrame.pack()
        
        buttonHeight=2
        buttonWidth=12
        
        Label(mainFrame, text="Joint").grid(row=0)
        Label(mainFrame, text="Angle (Degree)").grid(row=0, column=1)
        """
        
        e1 = Entry(mainFrame)
        e2 = Entry(mainFrame)
        
        e1.grid(row=1, column=0)
        e2.grid(row=1, column=1)
        """
        
        j=0
        for i in range(7):
            j=j+1
            labelName="J"+str(j)
            Label(mainFrame, text=labelName).grid(row=j, column=0)
            self.jText[i]=StringVar()
            self.jText[i].set("0.0")
            Entry(mainFrame,justify='center',textvariable=self.jText[i]).grid(row=j, column=1)
        
            if i==0:
                Label(mainFrame, text="    IP:").grid(row=j+1, column=3) 
                IPtxt=Entry(mainFrame,textvariable=self.IP_of_robot).grid(row=j+1, column=4)
                self.IP_of_robot.set("172.31.1.147")
            else:
                Label(mainFrame, text="      ").grid(row=j+1, column=3)   
        
        """The following is a space holder"""
        Label(mainFrame, text="    ").grid(row=j+1, column=0) 
        """ScrolledText(mainFrame).grid(columnspan=2)"""
        rowNum=1  
        Button(mainFrame,text="Connect",fg="red", command=self.connectFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=4)
        Button(mainFrame,text="turn off server",fg="red", command=self.disconnectFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="add new point",fg="red", command=self.addNewPointFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="delete last point",fg="red",command=self.removeLastPoint, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="perform program",fg="red",command=self.moveAllCommands, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="advance one step",fg="red",command=self.moveOnlyOneCommand, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="Go home",fg="red", command=self.homeFcn, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        rowNum=rowNum+1
        Button(mainFrame,text="About",fg="red",command=self.aboutFun, height = buttonHeight, width = buttonWidth).grid(row=rowNum,column=5)
        
        # Add the STATE MESSAGE textbox
        Label(mainFrame, text=" Msg").grid(row=8, column=0,sticky=W) 
        msgTxt=Entry(mainFrame,textvariable=self.stateMessage,width="40").grid(row=8, column=1,columnspan=4,rowspan=1,sticky=W)       
        #print(msgTxt.winfo_width())      
        self.stateMessage.set("Not connected")
        
        S = Scrollbar(root)
        T = Text(root, height=4, width=50)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        self.commandsText=T
        self.commandsScroll=S
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        try:
            root.mainloop()
        except:
            print('An error happened')
            print('Closing connection if opened')
            if self.connection_state:
                self.disconnectFun()
            
        
    def on_closing(self):
        if self.connection_state==False:
            self.root.destroy()
        else:
            self.disconnectFun()
            self.root.destroy()
        
    def connectFun(self):
        # Check if lready connected to the robot
        if self.connection_state:
            message="Already connected to the robot on IP: "+self.IP_of_robot.get()
            self.printMessage(message)
            return
        # If the program made it to here, then there is no connection yet
        message="Connecting to robot at ip: "+self.IP_of_robot.get()
        self.printMessage(message)
        try:
            self.iiwa=iiwaPy(self.IP_of_robot.get())
            self.connection_state=True
            message="Connection established succefully"
            self.printMessage(message)
        except:
            message="Error, could not connect at the specified IP"
            self.printMessage(message)
            return            
        jpos=self.iiwa.getJointsPos()
        for i in range(7):
            temp=jpos[i]*180/math.pi
            self.jText[i].set(str(temp))       
            # print "value of joint angle "+str(i)
            # print self.jText[i].get()
            
    def disconnectFun(self):
        # Check if there is an active connection
        if self.connection_state==False:
            message="Already off line"
            self.printMessage(message)
            return
        # If made it to here, then there is an active connection
        message="Disconnecting from robot"
        self.printMessage(message)
        # Try to disconnect        
        try:
            self.iiwa.close()
            self.connection_state=False
            message="Disconnected successfully"
            self.printMessage(message)
        except:
            message="Error could not disconnct"
            self.printMessage(message)
            return
        
    def homeFcn(self):
        # Check if there is an active connection
        if self.connection_state==False:
            message="Error, connect first"
            self.printMessage(message)
            return
        relVel=[0.1]
        self.iiwa.movePTPHomeJointSpace(relVel)
        
    def moveAllCommands(self):
        # Check if there is an active connection
        if self.connection_state==False:
            message="Error, connect first"
            self.printMessage(message)
            return
        n=len(self.commandsList)
        if n==0:
            message="No available commands to execute"
            self.printMessage(message)            
        for i in range(n):
            relVel=[0.1]
            jPos=self.commandsAngleList[0]
            self.iiwa.movePTPJointSpace(jPos,relVel)  
            self.removeFirstPoint()           
        
    def moveOnlyOneCommand(self):
        # Check if there is an active connection
        if self.connection_state==False:
            message="Error, connect first"
            self.printMessage(message)
            return
        if len(self.commandsList)>0:
            relVel=[0.1]
            jPos=self.commandsAngleList[0]
            self.iiwa.movePTPJointSpace(jPos,relVel)  
            self.removeFirstPoint()
        else:
            message="No available commands to execute"
            self.printMessage(message)
            
    def aboutFun(self):
        message="By Mohammad Safeea, 07-Oct-2019"
        self.printMessage(message)
            
    def addNewPointFun(self):
        # get value of joint angles from the textboxes (jText)
        jPosStr=''
        jPosFloatRads=[]
        for i in range(7):
            tempStr=self.jText[i].get()
            try:
                tempRad=float(tempStr)*math.pi/180
                jPosFloatRads.append(tempRad)
                jPosStr=jPosStr+tempStr+'_'
            except:
                message="Error in J["+str(i+1)+"] value"
                return
        # if made it to here, then everything is run successfully
        jPosStr=jPosStr+'\n'
        self.commandsList.append(jPosStr)
        self.commandsAngleList.append(jPosFloatRads)
        print(self.commandsAngleList)
        self.updateCommandsText()
    
    def removeLastPoint(self):
        if len(self.commandsList)>0:
            self.commandsList.remove(self.commandsList[-1])
            self.commandsAngleList.remove(self.commandsAngleList[-1])
            self.updateCommandsText()
            
    def removeFirstPoint(self):
        if len(self.commandsList)>0:
            self.commandsList.remove(self.commandsList[0])
            self.commandsAngleList.remove(self.commandsAngleList[0])
            self.updateCommandsText()
        
    def updateCommandsText(self):
        self.commandsText.delete('1.0', END)
        for item in self.commandsList:
            self.commandsText.insert(END, item)
        self.commandsText.see(END)
        
    def printMessage(self,message):
        # print message
        self.stateMessage.set(message)
             
Appliaction=App()
 




