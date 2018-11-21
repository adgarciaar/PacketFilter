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
        return w.check_filter(self.expression)
        
    def acceptTraffic(self,types):
        with pydivert.WinDivert(self.expression,1) as w:
            for packet in w:
                if ("tcp" in types):
                    if(packet.tcp != None):
                        w.send(packet)
                if ("udp" in types):
                    if(packet.udp != None):
                        w.send(packet)
                if ("icmp" in types):
                    if(packet.icmpv4 != None):
                        w.send(packet)                
    
    def blockTraffic(self):
        self.expression = self.expression
        with pydivert.WinDivert(self.expression,1) as w:        
            for packet in w:
                x = 0