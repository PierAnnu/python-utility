from utils.logger import Logger
log = Logger("Menu",4)


class Menu:
    def __init__(self, description, functions):
        log.hd("Menu Initialization")
        self.description = description
        self.functions = functions
        
    def run(self):
        log.hd("Menu Run")