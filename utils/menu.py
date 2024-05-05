# coding=utf-8

#version 0.081
#--------------------------------------------------
#Updates
#0.08 - Display class added
#0.072 - Now pressing e you will exit from menu
#0.071 - Not recognized actions will reload menu
#0.07 - Now menu can send a result after operations
#0.06 - Not integer will exit from menu
#0.05 - Added DynamicMenu, loop must be controlled outside
#0.04 - Minor fixing exiting menu, log position updated as default
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
    log = Logger(r"./logs/Menu",4)
    debug = False
    clear_on_load = False
    last_res = ""
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
            try:
                i = input(">")
                if i=='e':
                    self.log.hd(f"Exit menu riconosciuto")
                    return
                i = int(i)
            except Exception as E:
                self.log.hd(f"Opzione non riconosciuta, ricarico menu \n{E}")
                continue
            self.log.hd(f"Menu Choise: {i}")
            if (i>len(self.functions)-1 or i<0):
                self.log.d("Exiting menu")
                return 
            else:
                os.system('cls')
                if self.debug:
                    self.last_res = self.functions[i][1]()
                else:
                    try:
                        self.last_res = self.functions[i][1]()
                    except Exception as E:
                        self.log.e(f"Errori durante l'esecuzione di {self.functions[i][0]}\n{E}")
                        self.last_res = f"Error - {E}"

    def __show__(self):
        ctx = 0
        for fx in self.functions:
            self.log.i(f"{ctx}: {fx[0]} - {fx[1].__doc__}")
            ctx += 1
        self.log.i(f"LATEST> {self.last_res}")

class DynamicMenu(Menu):
    ''' Menu '''
    def __init__(self, description, functions):
        super().__init__(description,functions)
        self.log.hd("Menu Initialization")
        
    def run(self,dynamic_content):
        ''' Entra in Menu '''
        if self.clear_on_load:
            os.system('cls')
        self.log.hd("Menu Run")
        self.log.i(self.description)
        for d in dynamic_content:
            self.log.i(f"{d[0]} - {d[1]}")
        self.__show__()
        try:
            i = input(">")
            if i=='e':
                self.log.hd(f"Exit menu riconosciuto")
                return
            i = int(i)
        except Exception as E:
            self.log.hd(f"Opzione non riconosciuta, esco da menu\n{E}")
            return 0
        self.log.hd(f"Menu Choise: {i}")
        if (i>len(self.functions)-1 or i<0):
            self.log.d("Exiting menu")
            return -1
        else:
            os.system('cls')
            if self.debug:
                self.last_res = self.functions[i][1]()
                return 0
            else:
                try:
                    self.last_res = self.functions[i][1]()
                    return 0
                except Exception as E:
                    self.log.e(f"Errori durante l'esecuzione di {self.functions[i][0]}\n{E}")
                    self.last_res = f"Error - {E}"
                    return -1

class Display:
    """
    Classe per la gestione di un display a testo.

    Permette di aggiungere righe di testo che verranno visualizzate a video
    e di cancellare il contenuto precedente.
    """
    _lines = []
    _lines_init = []
    printfc = print

    def __init__(self):
        """
        Inizializza il display.
        """
        self._lines = []

    def add_line(self, txt, id):
        """
        Inizializza le righe di testo da mostrare a video.

        Args:
            txt: Il testo da aggiungere.
        """
        self._lines.append({"value":txt,"id":id})
        self._lines_init.append({"value":txt,"id":id})
        
    def new(self):
        self._lines = []
        self._lines_init = []

    def __show_list__(self,l:list):
        for t in l:
            self.__evalutate_type__(t)

    def __show_object__(self,o:dict):
        for k in o.keys():
            self.printfc(f"{k}: {o[k]}")

    def __evalutate_type__(self,val):
        ''' Stampa a video in base al tipo di dato ricevuto '''
        if type(val) == list:
            self.__show_list__(val)
        elif type(val) == dict:
            self.__show_object__(val)
        else:
            if val !="":
                self.printfc(val)

    def show(self):
        """
        Visualizza il contenuto del display a video.
        """
        self.clear()
        for line in self._lines:
            self.__evalutate_type__(line['value'])

    
    def update_line(self, line_id, updates):
        ''' Aggiorna la riga selezionata aggiungendo il valore aggiornato, e visualizza i dati aggiornati 
        Args:
            line_id: ID Linea.
            updates: Valore aggiornato
        '''
        for line in self._lines:
            if line['id'] == line_id:
                line['value'] = updates
        self.show()

    def reset(self):
        ''' Resetta le linee ai valori di impostazione
        '''
        self._lines = self._lines_init.copy()

    def clear(self):
        """
        Cancella il contenuto del display.
        """
        os.system('cls')
