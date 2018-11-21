# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:03:53 2018

@author: adrian
"""
class FileReader:
    
    def readRules(self, filename):

        fileRules = open(filename, "r")
        lines=fileRules.readlines()
        fileRules.close()
        
        print ("\nFile with rules read")
        
        counter = 0
        expression = ""
        counterIPs = 0
        counterConditions = 0
        numberLine = 0
        functionToUse = ""
        
        for line in lines:
            numberLine = numberLine + 1
            
            if(line[0] == "#"):
                counter = counter + 1
            else:

                if(counter == 1): #info de si es para aceptar o rechazar tráfico
                    functionToUse = line.rstrip()
                
                elif(counter == 2): #info de las IPs
                    
                    counterIPs = counterIPs + 1
                    IPs = line.rstrip().split("\t")
                    
                    if(len(IPs) == 2):
                        if(counterIPs > 1):
                            expression = expression + " and "
                        expression = expression + "ip." + IPs[1] + " == "+ IPs[0]
                    else:
                        print("Line "+str(numberLine)+" of the file is incorrect. It was ignored")
                    
                elif(counter == 3): #info de los protocolos
                    
                    counterConditions = counterConditions + 1
                    if(counterConditions == 1):
                        expression = expression + " and "
                        
                    conditions = line.rstrip().split("\t")

                    if(len(conditions) == 1 or len(conditions) == 2):

                        expression = expression + conditions[0] + "." + conditions[1]  + " " + conditions[2]
                        if(len(conditions) == 4):
                            expression = expression + " " + conditions[3]  
                        if( numberLine != len(lines) ):
                            expression = expression + " "
                    else:
                        print("Line "+str(numberLine)+" of the file is incorrect. It was ignored")
        
        return functionToUse, expression