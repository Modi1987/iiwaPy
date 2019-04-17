# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:21:02 2018

@author: Mohammad SAFEEA
"""
import socket
import time
import StringIO


class mySock:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, tup):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(tup)
        self.buff = StringIO.StringIO(2048)

    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        returnVal = []
        while True:
            data = self.sock.recv(1)
            if data == "\n":
                break
            self.buff.write(data)
        returnVal = self.buff.getvalue()
        self.buff.truncate(0)
        return returnVal

    def close(self):
        endCommand = "end\n"
        self.sock.send(endCommand)
        time.sleep(1)  # sleep for one seconds
        self.sock.close()
