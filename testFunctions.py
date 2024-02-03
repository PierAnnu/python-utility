from utils.logger import Logger
from utils import file
log = Logger(r"./TesterFunctions",4)

def test_read_file():
    ''' Funzione di verifica della lettura di un file '''
    log.hd("Test lettura file partito")
    file_name = input("File path:>")
    f = file.read(file_name)
    log.i(f"Test lettura file completato\n\n{f}")
    x = input("\nPress enter to continue")
    return

def test_write_file():
    ''' Funzione di verifica della scrittura di un file '''
    log.hd("Test scrittura file partito")
    file_name = input("File path:>")
    file.write(file_name,"w","Ciao")
    log.i(f"Test scrittura file completato, ho scritto 'ciao' in {file_name}")
    x = input("\nPress enter to continue")
    return