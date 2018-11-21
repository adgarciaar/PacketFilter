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
    """    
    def allowTraffic(self,protocols,ports):
        with pydivert.WinDivert(self.expression,1) as w:
            for packet in w:
                if ("tcp" in protocols):
                    if(packet.tcp != None):
                        if()
                        #if(packet.tcp.dst_port == 80)
                        w.send(packet)
                if ("udp" in protocols):
                    if(packet.udp != None):
                        w.send(packet)
                if ("icmp" in protocols):
                    if(packet.icmpv4 != None):
                        w.send(packet)   
    """        
    
    def blockTraffic(self):
        self.expression = self.expression
        with pydivert.WinDivert(self.expression,1) as w:        
            for packet in w:
                x = 0