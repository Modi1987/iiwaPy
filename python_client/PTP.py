# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 18:44:35 2018

@author: Mohammad SAFEEA
"""
import math
import StringIO
from Senders import Senders
from Getters import Getters


class PTP:
    def __init__(self, mysoc):
        self.mysoc = mysoc
        self.sender = Senders(mysoc)
        self.getter = Getters(mysoc)

    def send(self, data):
        data = data + "\n"
        self.mysoc.send(data)
        self.mysoc.receive()

    ## arcc motions
    def movePTPArc_AC(self, theta, c, k, vel):
        if len(c) <> 3:
            print("Error in function [movePTPArc_AC]")
            print("Center of circle should be an array of three lements")
            return
        if len(k) <> 3:
            print("Error in function [movePTPArc_AC]")
            print("Orientation vector should be an array of three lements")
            return
        if len(theta) <> 1:
            print("Error in function [movePTPArc_AC]")
            print("Angle of an arc should be a scalar")
            return
        if len(vel) <> 1:
            print("Error in function [movePTPArc_AC]")
            print("Relative velocity should be a scalar")
            return

        pos = self.getter.getEEFPos()
        x = (
            math.pow(c[0] - pos[0], 2)
            + math.pow(c[1] - pos[1], 2)
            + math.pow(c[2] - pos[2], 2)
        )
        r = math.pow(x, 0.5)
        if r == 0:
            print("Error in function [movePTPArc_AC]")
            print("radius can not be zero")
            return
        if theta == 0:
            print("Error in function [movePTPArc_AC]")
            print("angle can not be zero")
            return
        # calculate unit vector
        x = math.pow(k[0], 2) + math.pow(k[1], 2) + math.pow(k[2], 2)
        normK = math.pow(x, 0.5)
        if normK == 0:
            print("Error in function [movePTPArc_AC]")
            print("Norm of direction vector k shall not be zero")
            return
        k[0] = k[0] / normK
        k[1] = k[1] / normK
        k[2] = k[2] / normK
        s = [c[0] - pos[0], c[1] - pos[1], c[2] - pos[2]]
        s[0] = -s[0] / r
        s[1] = -s[1] / r
        s[2] = -s[2] / r
        n = [
            (k[1] * s[2] - k[2] * s[1]),
            (k[2] * s[0] - k[0] * s[2]),
            (k[0] * s[1] - k[1] * s[0]),
        ]
        c1 = self.rotTheThing(theta / 2, r, s, n, c)
        c2 = self.rotTheThing(theta, r, s, n, c)
        self.movePTPCirc1OrintationInter(c1, c2, vel)

    def rotTheThing(theta, r, s, n, c):
        c1 = [0, 0, 0]
        cos = math.cos(theta)
        sin = math.sin(theta)
        c1[0] = r * cos * s[0] + r * sin * n[0] + c[0]
        c1[1] = r * cos * s[1] + r * sin * n[1] + c[1]
        c1[2] = r * cos * s[2] + r * sin * n[2] + c[2]
        return c1

    def checkErrorInRelVel(self, relVel):
        if len(relVel) <> 1:
            print("Relative velocity should be a scalar")
            return True
        if relVel > 1:
            print("Relative velocity should be less than one")
            return True
        if relVel == 0:
            print("Relative velocity should be greater than zero")
            return True
        if relVel < 0:
            print("Relative velocity should be greater than zero")
            return True
        return False

    def movePTPArcXY_AC(self, theta, c, vel):
        if len(theta) <> 1:
            print("Error in function [movePTPArcXY_AC]")
            print("Roation angle should be a scalar")
            return
        if len(c) <> 2:
            print("Error in function [movePTPArcXY_AC]")
            print("Center of rotation should be an array of two elements [x,y]")
            return
        if len(vel) <> 1:
            print("Error in function [movePTPArcXY_AC]")
            print("Velocity should be a scalar")
            return
        k = [0, 0, 1]
        pos = self.getter.getEEFPos()
        c1 = [c, pos[2]]
        self.movePTPArc_AC(theta, c1, k, vel)

    def movePTPArcXZ_AC(self, theta, c, vel):
        if len(theta) <> 1:
            print("Error in function [movePTPArcXY_AC]")
            print("Roation angle should be a scalar")
            return
        if len(c) <> 2:
            print("Error in function [movePTPArcXY_AC]")
            print("Center of rotation should be an array of two elements [x,z]")
            return
        if len(vel) <> 1:
            print("Error in function [movePTPArcXY_AC]")
            print("Velocity should be a scalar")
            return
        k = [0, 1, 0]
        pos = self.getter.getEEFPos()
        c1 = [c[0], pos[1], c[1]]
        self.movePTPArc_AC(theta, c1, k, vel)

    def movePTPArcYZ_AC(self, theta, c, vel):
        if len(theta) <> 1:
            print("Error in function [movePTPArcYZ_AC]")
            print("Roation angle should be a scalar")
            return
        if len(c) <> 2:
            print("Error in function [movePTPArcYZ_AC]")
            print("Center of rotation should be an array of two elements [y,z]")
            return
        if len(vel) <> 1:
            print("Error in function [movePTPArcYZ_AC]")
            print("Velocity should be a scalar")
            return
        k = [1, 0, 0]
        pos = self.getter.getEEFPos()
        c1 = [pos[0], c[1], c[2]]
        self.movePTPArc_AC(theta, c1, k, vel)

    def movePTPCirc1OrintationInter(self, f1, f2, relVel):
        if len(f1) <> 6:
            print("Error in function [movePTPCirc1OrintationInter]")
            print(
                "The first frame should be an array of 6 lements [x,y,z,alpha,beta,gamma]"
            )
            return
        if len(f2) <> 6:
            print("Error in function [movePTPCirc1OrintationInter]")
            print(
                "The second frame should be an array of 6 lements [x,y,z,alpha,beta,gamma]"
            )
            return
        if len(relVel) <> 1:
            print("Error in function [movePTPCirc1OrintationInter]")
            print("Relative velocity should be a scalar")
            return
        buff = StringIO.StringIO(2048)
        buff.write("jRelVel_")
        buff.write(str(relVel))
        buff.write("_")
        buff.write("\n")
        command = buff.getvalue()
        self.send(command)
        self.sender.sendCirc1FramePos(f1)
        self.sender.sendCirc2FramePos(f2)
        theCommand = "doPTPinCSCircle1_"
        self.send(theCommand)

    def movePTPLineEEF(self, pos, vel):
        if len(vel) <> 1:
            print("Error in function [movePTPLineEEF]")
            print("Velocity shall be a scalar")
            return
        if len(pos) == 6:
            buff = StringIO.StringIO(2048)
            buff.write("jRelVel_")
            buff.write(str(vel))
            buff.write("_")
            buff.write("\n")
            command = buff.getvalue()
            self.send(command)
            self.sender.sendEEfPositions(pos)
            theCommand = "doPTPinCS\n"
            self.send(theCommand)
        else:
            print("Error in function [movePTPLineEEF]")
            print("Position should be an array of 6 elements")

    def movePTPLineEefRelEef(self, pos, vel):
        if len(vel) <> 1:
            print("Error in function [movePTPLineEefRelEef]")
            print("Velocity should be a scalar")
            return
        if len(pos) == 3:
            buff = StringIO.StringIO(2048)
            buff.write("jRelVel_")
            buff.write(str(vel))
            buff.write("_")
            buff.write("\n")
            command = buff.getvalue()
            self.send(command)
            newPos = [0, 0, 0, 0, 0, 0]
            newPos[0] = pos[0]
            newPos[1] = pos[1]
            newPos[2] = pos[2]
            self.sender.sendEEfPositions(newPos)
            theCommand = "doPTPinCSRelEEF\n"
            self.send(theCommand)
        else:
            print("Error in function [movePTPLineEefRelEef]")
            print("Position should be an array of 3 elements [x,y,z]")

    def movePTPLineEefRelBase(self, pos, vel):
        if len(pos) <> 3:
            print("Position should be an array of three lements [x,y,z]")
            return
        if len(vel) == 1:
            buff = StringIO.StringIO(2048)
            buff.write("jRelVel_")
            buff.write(str(vel))
            buff.write("_")
            buff.write("\n")
            command = buff.getvalue()
            self.send(command)
            newPos = [0, 0, 0, 0, 0, 0, 0]
            newPos[0] = pos[0]
            newPos[1] = pos[1]
            newPos[2] = pos[2]
            self.sender.sendEEfPositions(newPos)
            theCommand = "doPTPinCSRelBase\n"
            self.send(theCommand)
        else:
            print("Velocity should be a scalar")

    # joint space
    def movePTPJointSpace(self, jpos, relVel):
        if len(jpos) <> 7:
            print("Error in function [movePTPHomeJointSpace]")
            print("Joints positions shall be an array of 7 elements")
            return
        if len(relVel) == 1:
            buff = StringIO.StringIO(2048)
            buff.write("jRelVel_")
            buff.write(str(relVel))
            buff.write("_")
            buff.write("\n")
            command = buff.getvalue()
            self.send(command)
            self.sender.sendJointsPositions(jpos)
            theCommand = "doPTPinJS\n"
            self.send(theCommand)
        else:
            print("Error in function [movePTPHomeJointSpace]")
            print("Relative velocity should be a scalar")

    def movePTPHomeJointSpace(self, relVel):
        if len(relVel) == 1:
            buff = StringIO.StringIO(2048)
            buff.write("jRelVel_")
            buff.write(str(relVel))
            buff.write("_")
            buff.write("\n")
            command = buff.getvalue()
            self.send(command)
            jpos = [0, 0, 0, 0, 0, 0, 0]
            self.sender.sendJointsPositions(jpos)
            theCommand = "doPTPinJS\n"
            self.send(theCommand)
        else:
            print("Error in function [movePTPHomeJointSpace]")
            print("Relative velocity should be a scalar")

    def movePTPTransportPositionJointSpace(self, relvel):
        if len(relvel <> 1):
            print("Error in function [movePTPHomeJointSpace]")
            print("Relative velocity should be a scalar")
            return
        jpos = [0, 0, 0, 0, 0, 0, 0]
        jpos[3] = 25 * math.pi / 180
        jpos[5] = 90 * math.pi / 180
        self.movePTPJointSpace(jpos, relvel)
