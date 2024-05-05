# coding=utf-8

#version 0.0
#--------------------------------------------------
#Updates
#0.0 - Initial file version
#--------------------------------------------------
#Description
#Networker helper functions
#--------------------------------------------------

import subprocess
from time import sleep
import requests
from utils.logger import Logger
logger = Logger(".\logs\_networker",3)


def check_ping(ip):
  """
  Effettua un ping a un indirizzo IP per verificarne la connessione.

  Args:
    ip: l'indirizzo IP da testare.

  Returns:
    True se l'indirizzo IP è raggiungibile, False altrimenti.
  """
  # Esegue il comando ping.
  response = subprocess.run(['ping', '-n', '1', ip], capture_output=True)
  # Controlla il codice di uscita.
  if response.returncode == 0:
    return True
  else:
    return False

def is_connection_active(host='http://192.168.1.1'):
    ''' Funzione che verifica se la connessione è attiva, 
    manda una richiesta all'host (solitamente il modem) 
    se questo risponde la connessione viene considerata attiva '''
    try:
        response = requests.get(host)
        return True
    except Exception as E:
        logger.d(E)
        pass
    return False

def reconnect_wifi(wifi_ssid):
    ''' Funzione che si riconnette al wifi indicato '''
    # Nome della rete WiFi da connettersi
    #wifi_ssid = "nome_rete_wifi"

    # Comando per ottenere l'elenco delle reti WiFi salvate sul PC
    wifi_profiles_command = "netsh wlan show profiles"

    # Esecuzione del comando per ottenere l'elenco delle reti WiFi
    wifi_profiles_output = subprocess.check_output(wifi_profiles_command, shell=True)

    # Decodifica dell'output in una stringa
    wifi_profiles_output = wifi_profiles_output.decode('utf-8')

    # Ottenere il nome delle reti WiFi salvate dal comando di output
    wifi_profile_names = [line.split(":")[1][1:-1] for line in wifi_profiles_output.split("\n") if "Tutti i profili utente" in line]
    logger.d(wifi_profile_names)
    # Controlla se la rete WiFi specificata esiste tra quelle salvate
    if wifi_ssid in wifi_profile_names:
        logger.d(f"La rete WiFi '{wifi_ssid}' è stata trovata.")
        
        # Comando per connettersi alla rete WiFi specificata
        connect_command = f'netsh wlan connect name="{wifi_ssid}"'

        # Esecuzione del comando per connettersi alla rete WiFi
        connect_output = subprocess.check_output(connect_command, shell=True)

        # Decodifica dell'output in una stringa
        connect_output = connect_output.decode('utf-8')
        # Verifica se la connessione alla rete WiFi è riuscita
        if "Richiesta di connessione completata" in connect_output:
            logger.i(f"Connessione alla rete WiFi '{wifi_ssid}' riuscita.")
            sleep(1)
        else:
            logger.e(f"Errore durante la connessione alla rete WiFi '{wifi_ssid}'.")
    else:
        logger.w(f"La rete WiFi '{wifi_ssid}' non è stata trovata tra quelle salvate.")
