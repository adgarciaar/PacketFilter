# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:03:53 2018

@author: adrian
"""


class FileReader:

    def readRules(self, filename):

        fileRules = open(filename, "r")
        lines = fileRules.readlines()
        fileRules.close()

        print("\nFile with rules read")

        expression = None
        instruction = None

        if(len(lines) > 1):

            type = ""
            expression = ""
            counterIPs = 0
            counterConditions = 0
            numberLine = 0

            for line in lines:

                numberLine = numberLine + 1

                if(line[0] == "#"):
                    if(line.rstrip() == "#Instruction"):
                        type = "Instruction"
                    elif(line.rstrip() == "#IPs"):
                        type = "IPs"
                    elif(line.rstrip() == "#Protocols"):
                        type = "Protocols"
                else:

                    if(type == "Instruction"):  # info de si es para aceptar o rechazar tráfico
                        if (line.rstrip() == "block all"):
                            expression = "true"
                            instruction = "block"
                            break
                        elif(line.rstrip() == "block"):
                            instruction = "block"
                        elif(line.rstrip() == "true"):
                            instruction = "true"

                    if(type == "IPs"):  # info de las IPs

                        counterIPs = counterIPs + 1
                        if(counterIPs == 1):
                            expression = expression + "("
                        IPs = line.rstrip().split("\t")

                        if(len(IPs) == 2):
                            if(counterIPs > 1):
                                expression = expression + " or "
                            expression = expression + "ip." + \
                                IPs[1] + " == " + IPs[0]
                        else:
                            print("Line "+str(numberLine) +
                                  " of the file is incorrect. It was ignored")

                        if(numberLine == len(lines)):
                            expression = expression + ")"

                    elif(type == "Protocols"):  # info de los protocolos

                        counterConditions = counterConditions + 1
                        if(counterConditions == 1 and counterIPs > 0):
                            expression = expression + ") and ("

                        conditions = line.rstrip().split("\t")

                        if(len(conditions) == 1 or len(conditions) == 2):

                            expression = expression + conditions[0]

                            if(len(conditions) == 2):
                                expression = expression + "." + conditions[1]

                            if(numberLine < len(lines)):
                                expression = expression + " or "

                            if(numberLine == len(lines) and counterIPs > 0):
                                expression = expression + ")"

                        else:
                            print("Line "+str(numberLine) +
                                  " of the file is incorrect. It was ignored")

            if(expression == ""):
                expression = None

        return expression, instruction
