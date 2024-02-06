# coding=utf-8

#version 0.04
#--------------------------------------------------
#Updates
#0.04 - log position updated, added reboot function after update
#0.03 - Logger moved inside class to get better control on logging
#0.02 - Major Fixing
#0.01 - Initial Version
#--------------------------------------------------
#Description
# VERIFICA SU GITHUB VARI APPLICATIVI PER CONTROLLARE NUOVE VERSIONI
# IN CASO TROVA NUOVE VERSIONI DEGLI APPLICATIVI LI SCARICA E LI AGGIORNA
#--------------------------------------------------

from utils.logger import Logger
from utils import file
import requests
import os
import sys

class Updater:
    configuration_path= r"./config/updater_configuration.json"
    log = Logger(r"./logs/Updater",4)
    def __init__(self):
        self.log.hd("Inizializzazione Updater")

    def check_updates(self):
        ''' Verifica aggiornamenti file '''
        self.log.hd("Inizio verifica aggiornamenti")
        # File List composta da [0] Path, [1] Release
        fl = file.readJSON(self.configuration_path)
        for f in fl:
            url = f[1]
            content = self.__download_content__(url)
            # Salva il contenuto in un file
            content_l = str(content,encoding="utf-8").split('\n')
            version = content_l[2]
            release_version = float(version[8:])
            actual = file.read(f[0])
            actual = actual.split('\n')
            actual_version = actual[2]
            actual_version = float(actual_version[8:])
            self.log.hd(f"Identificati i seguenti dati per {f[0]}\nVersione attuale {actual_version}, versione release {release_version}")
            if actual_version<release_version:
                self.log.i(f"Aggiorno file {f[0]}")
                file.write(fr"{f[0]}","wb",content)
                self.__reboot__()
            elif actual_version == release_version:
                self.log.i(f"File {f[0]} già aggiornato")
            else:
                self.log.w("La tua versione è più aggiornata della release! Aggiorna la release!")
        self.log.i("Aggiornamento completato")


    def __reboot__(self):
        """Funzione per riavviare il programma in esecuzione."""
        os.execv(sys.executable, ['python'] + sys.argv)

    def __download_content__(self,url):
        """
        Funzione per scaricare contenuto dal web

        Args:
            url (str): URL del contenuto da scaricare

        Returns:
            bytes: Contenuto scaricato
        """

        # Invia una richiesta GET all'URL
        response = requests.get(url)

        # Controlla lo stato della risposta
        if response.status_code == 200:
            # Ritorna il contenuto scaricato
            return response.content
        else:
            # Errore durante la richiesta
            raise RuntimeError(f"Errore durante la richiesta: {response.status_code}")


        