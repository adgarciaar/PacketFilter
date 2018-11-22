# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:09:38 2018

@author: adrian
"""

import pydivert


class Firewall:

    def __init__(self, expression):
        self.expression = expression

    def validateExpression(self):
        w = pydivert.WinDivert(self.expression)
        x, y, z = w.check_filter(self.expression)
        return z

    def allowTraffic(self):
        with pydivert.WinDivert("true", 1) as w:
            for packet in w:
                if (packet.matches(self.expression, 1) == True):
                    w.send(packet, True)

    def blockTraffic(self):
        with pydivert.WinDivert("true", 1) as w:
            for packet in w:
                if (packet.matches(self.expression, 1) == False):
                    w.send(packet, True)
