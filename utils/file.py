# coding=utf-8

#version 0.341
#--------------------------------------------------
#Updates
#0.341 - Added clearDir docs 
#0.34 - Write File correctly accept binary writing 
#0.33 - New function for reading file details 
#0.32 - Improvement for enconding during reading json 
#0.31 - Improvement for import library 
#0.3 - Updated sequence of path, mode, data in writes function 
#0.211 - minor update, fix import csv on header
#0.21 - Add delete function : Delete a file
#--------------------------------------------------
#Description
#Easier File Manager
#--------------------------------------------------

import json
import os
import csv
import shutil




def CSVToXLS(path,newpath):
    from xlsxwriter.workbook import Workbook
    workbook = Workbook(newpath)
    worksheet = workbook.add_worksheet()
    with open(path, 'rt', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()

def fileList(path):
    return os.listdir(path)

def readFileDetails(filepath):
    ''' Return an object containing file details
        st_mode: the file type and permissions
        st_ino: the inode number
        st_dev: the device id
        st_uid: the file owner id
        st_gid: the file group id
        st_size: the file size
    '''
    return os.stat(filepath)
    
def delete(path):
    try:
        os.remove(fr"{path}")
        return True
    except FileNotFoundError:
        return False
        
def clearDir(path):
  """
  Funzione che cancella tutti i file in una cartella.

  Args:
      path (str): Percorso della cartella da cui cancellare i file.

  Raises:
      OSError: Se la cartella non esiste o non è possibile eliminarla.
  """
  for e in os.listdir(path):
    os.remove(fr"{path}/{e}")

def createDir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        # clearDir(path)
        pass

def readJSON(path, encoding='utf-8'):
    ''' Legge un Json, ritorna {} se questo non esiste '''
    r = {}
    if os.path.exists(path):
        with open(path, "r", encoding=encoding) as f:
            r = json.load(f)
            f.close()
    return r
    
def writeJSON(path, mode, data):
    with open(path, mode) as f:
        f.write(json.dumps(data))
        f.close()

def readCSV(path):
    """
    Legge un file CSV con separatore ";" e ritorna una lista di array.

    :param path: Il nome del file CSV da leggere.
    :type path: str
    :return: Una lista di array, dove ogni array rappresenta una riga del file CSV.
    :rtype: list[list]
    """
    with open(path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = []
        for row in reader:
            # Unisce eventuali valori multipli in una cella
            row = [str(cell.replace('\n', '|||')) for cell in row]
            data.append(row)
        return data

def writeCSV(path, mode, data):
    """
    Scrive un file CSV con separatore ";" a partire da una lista di array.

    :param data: La lista di array da scrivere nel file CSV.
    :type data: list[list]
    :param path: Il nome del file CSV da scrivere.
    :type path: str
    """
    with open(path, mode=mode, newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"')
        for row in data:
            # Sostituisce eventuali spazi vuoti con il carattere di newline
            row = [str(cell.replace('|||', '\n')) for cell in row]
            writer.writerow(row)
    
def read(path):
    r = ""
    with open(path, "r", encoding='utf-8') as f:
        r = f.read()
        f.close()
    return r
    
def write(path, mode, data,encoding="utf-8"):
    if mode.find("b") != -1:
        with open(path, mode) as f:
            f.write(data)
        f.close()
        return
    with open(path, mode, encoding=encoding) as f:
        f.write(data)
    f.close()
    return
    
def copy(source,destination):
    shutil.copy(source, destination)