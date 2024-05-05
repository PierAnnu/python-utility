import time
from datetime import datetime
import asyncio
from utils.logger import Logger

logger = Logger("./logs/timer",3)

class Timer():
    ''' Classe Timer, permette di costrutire un timer.
    wait - Secondi di attesa
    per far partire il timer è necessario eseguire la funzione run
    è possibile tramite check verificare se il tempo di esecuzione è passto,
    tramite sleep attendere fino al tempo di esecuzione '''
    def __init__(self, wait):
        self.wait = wait
        self.start = 0
        self._firstExecution = False
    
    def elapsed(self):
        ''' Funzione che ritorna il tempo trascorso da quando il timer è partito '''
        ct = time.time()
        return ct - self.start
    
    def missing(self):
        ''' Funzione che ritorna il tempo mancante alla fine del timer '''
        return self.wait - self.elapsed()

    def check(self):
        ''' Ritorna True se il tempo di attesa è trascorso dallo start '''
        ct = time.time()
        if ct - self.start >= self.wait:
            return True
        return False

    def sleep(self):
        ''' Attende fino al tempo impostato da quanto il timer è partito'''
        while(not(self.check())):
            time.sleep(0.1)
           
    def semaphore(self):
        if self.check() or self._firstExecution == False:
            self.run()
            self._firstExecution = True
            return True
        else:
            return False
    
    def minisleep(self, p_in="", p_end="",p_over="Fine", microdelay=0.05,printfc=print) -> None:
        ''' 
        p_in: Frase in ingresso dell'attesa
        p_end: Frase in uscita dell'attesa
        p_over: Frase finale dopo l'attesa
        Funzione di attesa + print di una frase + tempo mancante '''
        while not(self.check()):
            time.sleep(microdelay)
            printfc(f"{p_in} {self.missing():.2f}{p_end}",end="\r")
        printfc(f"{p_over}"+('    '*int(((len(p_in)+len(p_end)-len(p_over)+5)/4)+1)))
        return
        
    async def async_sleep(self):
        ct = time.time()
        if ct - self.start <= self.wait:
            w = self.wait - (ct - self.start)
            await asyncio.sleep(w)

    def run(self):
        ''' Funzione di avviamento del timer. '''
        self.start = time.time()
        

## OUTSIDE CLASS
def time_to_str(timestamp):
    """
    Converte un timestamp in intero in una stringa con formato dd/mm/aaaa hh/mm/ss.

    Args:
        timestamp: Timestamp in intero.

    Returns:
        Stringa con formato dd/mm/aaaa hh/mm/ss.
    """

    # Convertiamo il timestamp in un oggetto datetime
    if type(timestamp)==int:
        dt = datetime.fromtimestamp(timestamp/1000)
    else:
        dt = datetime.fromtimestamp(timestamp)

    # Restituiamo la stringa formattata
    return dt.strftime("%d/%m/%Y %H:%M:%S")

def get_minutes(timex=time.time()):
  """
  Funzione che estrae i minuti dal tempo dato in input.
    input: int|float - Valore tempo
  Returns:
    int: I minuti del timestamp corrente.
  """
  # Otteniamo il timestamp corrente
  if type(timex)==int:
      timex = timex/1000
  # Convertiamo il timestamp in un oggetto datetime
  dt = datetime.fromtimestamp(timex)
  # Estraiamo i minuti dall'oggetto datetime
  minuti = dt.minute
  return minuti

def isToday(time_int):
    ''' Funzione che ritorna se un determinato tempo è oggi '''
    logger.d(f"Elapsed time: {time.time() - time_int/1000}")
    return ((time.time() - (time_int/1000)) < 86400)

def now():
    return time.time()