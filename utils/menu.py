# coding=utf-8

#version 0.01
#--------------------------------------------------
#Updates
#0.01 - Initial Version
#--------------------------------------------------
#Description
#Simple Menu Interface
#--------------------------------------------------

from utils.logger import Logger
log = Logger("Menu",4)


class Menu:
    ''' Menu '''
    debug = False
    def __init__(self, description, functions):
        log.hd("Menu Initialization")
        self.description = description
        self.functions = functions
        
    def run(self):
        ''' Entra in Menu '''
        while(1):
            log.hd("Menu Run")
            log.i(self.description)
            self.__show__()
            i = int(input(">"))
            log.hd(f"Menu Choise: {i}")
            if (i>len(self.functions) or i<0):
                log.d("Exiting menu")
                return
            else:
                if self.debug:
                    self.functions[i][1]()
                else:
                    try:
                        self.functions[i][1]()
                    except Exception as E:
                        log.e(f"Errori durante l'esecuzione di {self.functions[i][0]}\n{E}")

    def __show__(self):
        ctx = 0
        for fx in self.functions:
            log.i(f"{ctx}: {fx[0]} - {fx[1].__doc__}")
            ctx += 1
