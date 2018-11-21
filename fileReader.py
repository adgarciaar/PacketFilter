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

        #protocols = []
        #ports = []

        if( len(lines) == 0 ):
            expression = None
            #functionToUse = None

        elif( len(lines) == 1 ):
            if ( lines[0].rstrip() == "block all" ):
                expression = "true"
                #functionToUse = "block all"
            else:
                expression = None
                #functionToUse = None
        
        else:
        
            counter = 0
            expression = ""
            counterIPs = 0
            counterConditions = 0
            numberLine = 0
            #functionToUse = ""
            #allowTraffic = False
            
            for line in lines:

                numberLine = numberLine + 1
                
                if(line[0] == "#"):
                    counter = counter + 1
                else:

                    #if(counter == 1): #info de si es para aceptar o rechazar tráfico
                    #    functionToUse = line.rstrip()
                        #if(functionToUse == "allow"):
                        #    allowTraffic = True
                    
                    if(counter == 1): #info de las IPs
                        
                        counterIPs = counterIPs + 1
                        IPs = line.rstrip().split("\t")
                        
                        if(len(IPs) == 2):
                            if(counterIPs > 1):
                                expression = expression + " or "
                            expression = expression + "ip." + IPs[1] + " == "+ IPs[0]
                        else:
                            print("Line "+str(numberLine)+" of the file is incorrect. It was ignored")
                        
                    elif(counter == 2): #info de los protocolos
                        
                        counterConditions = counterConditions + 1
                        if(counterConditions == 1):
                            expression = expression + " and "
                            
                        conditions = line.rstrip().split("\t")
                        print(conditions)

                        if(len(conditions) == 1 or len(conditions) == 2):

                            """
                            if(allowTraffic == True):
                                protocols.append(conditions[0])
                                ports.append(conditions[1])
                            """
                            
                            expression = expression + conditions[0]

                            if(len(conditions) == 2):
                                expression = expression + "." + conditions[1]

                            if( numberLine != len(lines) ):
                                expression = expression + " and "

                        else:
                            print("Line "+str(numberLine)+" of the file is incorrect. It was ignored")

            if(expression == ""):
                expression = None
            #if(functionToUse == ""):
            #    functionToUse = None

        """
        if(len(protocols) == 0):
            protocols = None
        if(len(ports) == 0):
            ports = None
        """
        return expression
        #return functionToUse, expression, protocols, conditions