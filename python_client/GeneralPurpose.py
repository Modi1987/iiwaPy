# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:45:29 2018

@author: Mohammad SAFEEA
"""

import sys


def getDoubleFromString(message, size):
    strVals = message.split("_")
    doubleVals = []
    counter = 0
    for strVal in strVals:
        counter = counter + 1
        if counter > size:
            break
        try:
            x = float(strVal)
            doubleVals.append(x)
        except:
            print("can not convert the following variable to float")
            print(strVal)
            sys.stdout.flush()

    return doubleVals


def directKinematics(q):
    if len(q) <> 7:
        print("Error in function [directKinematics]")
        print("The size of the joint angles shall be 7")
        return
