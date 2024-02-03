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
    def __init__(self, description, functions):
        log.hd("Menu Initialization")
        self.description = description
        self.functions = functions
        
    def run(self):
        while(1):
            log.hd("Menu Run")
            log.i(self.description)
            self._show()
            i = int(input(">"))
            log.hd(f"Menu Choise: {i}")
            if (i>len(self.functions) or i<0):
                log.d("Exiting menu")
                return
            else:
                try:
                    self.functions[i][1]()
                except Exception as E:
                    log.e(f"Errori durante l'esecuzione di {self.functions[i][0]}\n{E}")

    def _show(self):
        ctx = 0
        for fx in self.functions:
            log.i(f"{ctx}: {fx[0]} - {fx[1].__doc__}")
            ctx += 1
