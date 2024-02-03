# VERIFICA SU GITHUB VARI APPLICATIVI PER CONTROLLARE NUOVE VERSIONI
# IN CASO TROVA NUOVE VERSIONI DEGLI APPLICATIVI LI SCARICA E LI AGGIORNA

from utils.logger import Logger
from utils import file
log = Logger(r"./Updater",4)
import requests

class Updater:
    configuration_path= r"./config/updater_configuration.json"

    def __init__(self):
        log.hd("Inizializzazione Updater")

    def check_updates(self):
        ''' Verifica aggiornamenti file '''
        log.hd("Inizio verifica aggiornamenti")
        # File List composta da [0] Path, [1] Release
        fl = file.readJSON(self.configuration_path)
        for f in fl:
            url = f[1]
            content = self.__download_content__(url)
            # Salva il contenuto in un file
            content = str(content,encoding="utf-8").split('\n')
            version = content[2]
            release_version = float(version[8:])
            actual = file.read(f[0])
            actual = actual.split('\n')
            actual_version = actual[2]
            actual_version = float(actual_version[8:])
            log.hd(f"Identificati i seguenti dati per {f[0]}\nVersione attuale {actual_version}, versione release {release_version}")
            if actual_version<release_version:
                log.i(f"Aggiorno file {f[0]}")
            elif actual_version == release_version:
                log.i(f"File {f[0]} già aggiornato")
            else:
                log.w("La tua versione è più aggiornata della release! Aggiorna la release!")
        log.i("Aggiornamento completato")
                    
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


        