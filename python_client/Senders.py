# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:36:18 2018

@author: Mohammad SAFEEA
"""

import StringIO
import math
from GeneralPurpose import getDoubleFromString


class Senders:
    def __init__(self, mysoc):
        self.mysoc = mysoc

    def send(self, data):
        data = data + "\n"
        self.mysoc.send(data)
        message = self.mysoc.receive()
        return message

    def sendEEfPositions(self, x):
        if len(x) <> 6:
            print("Error in sender function [sendEEfPositions]")
            print("EEF position shall be an array of 6 elements")
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("cArtixanPosition_")
        counter = 0
        while counter < 6:
            buff.write(str(math.ceil(x[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        self.send(command)

    def sendJointsPositions(self, x):
        if len(x) <> 7:
            print("Error in sender function [sendJointsPositions]")
            print("Joint positions shall be an array of 7 elements")
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("jp_")
        counter = 0
        while counter < 7:
            buff.write(str(math.ceil(x[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        self.send(command)

    def sendJointsPositionsGetMTorque(self, x):
        if len(x) <> 7:
            print("Error in sender function [sendJointsPositionsGetMTorque]")
            print("Joint positions shall be an array of 7 elements")
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("jpMT_")
        counter = 0
        while counter < 7:
            buff.write(str(math.ceil(x[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        return getDoubleFromString(self.send(command), 7)

    def sendJointsPositionsGetExTorque(self, x):
        if len(x) <> 7:
            print("Error in sender function [sendJointsPositionsGetExTorque]")
            print("Joint positions shall be an array of 7 elements")
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("jpExT_")
        counter = 0
        while counter < 7:
            buff.write(str(math.ceil(x[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        return getDoubleFromString(self.send(command), 7)

    def sendJointsPositionsGetActualJpos(self, x):
        if len(x) <> 7:
            print("Error in sender function [sendJointsPositionsGetActualJpos]")
            print("Joint positions shall be an array of 7 elements")
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("jpJP_")
        counter = 0
        while counter < 7:
            buff.write(str(math.ceil(x[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        return getDoubleFromString(self.send(command), 7)

    def sendCirc1FramePos(self, fpos):
        if len(fpos) <> 6:
            print("Error in sender function [sendCirc1FramePos]")
            print(
                "Frame cooridnate is an array of 6 elements [x,y,z,alpha,beta,gamma] "
            )
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("cArtixanPositionCirc1_")
        counter = 0
        while counter < 6:
            buff.write(str(math.ceil(fpos[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        self.send(command)

    def sendCirc2FramePos(self, fpos):
        if len(fpos) <> 6:
            print("Error in sender function [sendCirc2FramePos]")
            print(
                "Frame cooridnate is an array of 6 elements [x,y,z,alpha,beta,gamma] "
            )
            return
        num = 10000
        buff = StringIO.StringIO(2048)
        buff.write("cArtixanPositionCirc2_")
        counter = 0
        while counter < 6:
            buff.write(str(math.ceil(fpos[counter] * num) / num))
            buff.write("_")
            counter = counter + 1
        buff.write("\n")
        command = buff.getvalue()
        self.send(command)
