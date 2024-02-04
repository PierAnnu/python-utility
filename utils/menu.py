# coding=utf-8

#version 0.03
#--------------------------------------------------
#Updates
#0.03 - Logger moved inside class to get better control on logging, added clear support for windows
#0.02 - Implemented debug
#0.01 - Initial Version
#--------------------------------------------------
#Description
#Simple Menu Interface
#--------------------------------------------------

from utils.logger import Logger
import os

class Menu:
    ''' Menu '''
    log = Logger("Menu",4)
    debug = False
    clear_on_load = False
    def __init__(self, description, functions):
        self.log.hd("Menu Initialization")
        self.description = description
        self.functions = functions
        
    def run(self):
        ''' Entra in Menu '''
        while(1):
            if self.clear_on_load:
                os.system('cls')
            self.log.hd("Menu Run")
            self.log.i(self.description)
            self.__show__()
            i = int(input(">"))
            self.log.hd(f"Menu Choise: {i}")
            if (i>len(self.functions) or i<0):
                self.log.d("Exiting menu")
                return
            else:
                if self.debug:
                    self.functions[i][1]()
                else:
                    try:
                        self.functions[i][1]()
                    except Exception as E:
                        self.log.e(f"Errori durante l'esecuzione di {self.functions[i][0]}\n{E}")

    def __show__(self):
        ctx = 0
        for fx in self.functions:
            self.log.i(f"{ctx}: {fx[0]} - {fx[1].__doc__}")
            ctx += 1
