# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:03:53 2018

@author: adrian
"""
class FileReader:
    
    #def __init__(self):        
    
    def readRules(self, filename): 
        fileRules = open(filename, "r")
        lines=fileRules.readlines()
        fileRules.close() 
        
        print ("\n File with rules read\n")
        
        counter = 0
        expression = ""
        counterIPs = 0
        counterConditions = 0
        numberLine = 0
        
        for line in lines:
            numberLine = numberLine + 1
            
            if(line[0] == "#"):
                counter = counter + 1
            else:
                
                if(counter == 1):
                    
                    counterIPs = counterIPs + 1
                    IPs = line.rstrip().split("\t")
                    if(counterIPs > 1):
                        expression = expression + " and "
                    expression = expression + "ip." + IPs[1] + " == "+ IPs[0]
                    
                elif(counter == 2):
                    
                    counterConditions = counterConditions + 1
                    if(counterConditions == 1):
                        expression = expression + " and "
                        
                    conditions = line.rstrip().split("\t")
                    expression = expression + conditions[0] + "." + conditions[1]  + " " + conditions[2]
                    if(len(conditions) == 4):
                        expression = expression + " " + conditions[3]  
                    if( numberLine != len(lines) ):
                        expression = expression + " "
        
        return expression

