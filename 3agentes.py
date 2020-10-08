import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False
semaforo = threading.Semaphore()

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    semaforo.acquire()
    while True:
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papelEnMesa = True
            tabacoEnMesa = True
        if caso == 1:
            papelEnMesa = True
            fosforosEnMesa = True
        if caso == 2:
            fosforosEnMesa = True
            tabacoEnMesa = True
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    while True:
        # si hay fósforos y tabaco en la mesa
        if 0 :
            papelEnMesa = False
            tabacoEnMesa = False
            print('fumar papel')
            time.sleep(2)
            semaforo.release()

      

def fumadorConFosforos():
    while True:
        # si hay papel y tabaco en la mesa
        if 1 :
            papelEnMesa = False
            tabacoEnMesa = False
            print('fumar fosforo')
            time.sleep(2)
            semaforo.release()
          

def fumadorConTabaco():
    while True:
        # si hay fósforos y papel en la mesa
        if 2:
            fosforosEnMesa = False
            papelEnMesa = False
            print('fumar tabaco')
            time.sleep(2)
            semaforo.release()
        


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

