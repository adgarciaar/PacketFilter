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
        
    def acceptTraffic(self):
        with pydivert.WinDivert(self.expression) as w:
            for packet in w:
                #revisar esta parte para redes externas
                if(packet.dst_addr != '10.0.0.2' and packet.dst_addr == '20.0.0.2'):
                    packet.src_addr = '30.0.0.1'
                w.send(packet)
    
    def blockTraffic(self):
        x = 1
        with pydivert.WinDivert(self.expression) as w:        
            for packet in w:
                x = 0