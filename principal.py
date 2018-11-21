# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:15:46 2018

@author: adrian
"""

from fileReader import FileReader
from firewall import Firewall

from pathlib import Path #para conseguir el path completo del archivo
import os.path #para verificar si el archivo existe

class Principal:

    def main(self):

        # solicitar nombre del archivo (debe estar en el misma carpeta)
        print('Write the file name with extension (e.g. rules.txt):')
        filename = input()

        # obtener direccion absoluta del archivo:
        # https://stackoverflow.com/questions/12201928/python-open-gives-ioerror-errno-2-no-such-file-or-directory
        script_location = Path(__file__).absolute().parent
        file_location = script_location / filename
        # print(file_location)

        # si el archivo existe la ejecución continúa
        #https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
        if(os.path.exists(file_location) == True):

            # leer expresión según el archivo de reglas
            reader = FileReader()
            functionToUse, expression = reader.readRules(file_location)
            print("\nExpression to filter: "+expression)

            # hacer lo nuestro
            firewall = Firewall(expression)
            x, y, z = firewall.validateExpression()
            if (z == "No error"):  # la expresión es correcta
                if(functionToUse == "accept"):
                    firewall.acceptTraffic()
                elif(functionToUse == "block"):
                    firewall.acceptTraffic()
            else:
                print("The expression is wrong according to WinDivert rules")

        else: # si el archivo no existe se termina la ejecución
            print("The file doesn't exist")

if __name__ == "__main__":
    principal = Principal()
    principal.main()