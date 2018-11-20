# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:15:46 2018

@author: adrian
"""

from fileReader import FileReader
from firewall import Firewall

from pathlib import Path

def main():
    #obtener direccion absoluta del archivo: 
    #https://stackoverflow.com/questions/12201928/python-open-gives-ioerror-errno-2-no-such-file-or-directory
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'rules.txt'
    #print(file_location)

    #leer expresión según el archivo de reglas
    reader = FileReader()
    expression = reader.readRules(file_location)
    print(expression)

    #hacer lo nuestro
    firewall = Firewall(expression)
    print(firewall.validateExpression())
    #firewall.acceptTraffic()

if __name__ == "__main__":
    main()