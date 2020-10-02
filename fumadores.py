import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

semaforoAgente = threading.Semaphore(1)
semaforoPapel = threading.Semaphore(1)
semaforoTabaco = threading.Semaphore(1)
semaforoFosforo = threading.Semaphore(1)

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papelEnMesa = True
            tabacoEnMesa = True
            semaforoPapel.release()
            semaforoTabaco.release()
        if caso == 1:
            papelEnMesa = True
            fosforosEnMesa = True
            semaforoPapel.release()
            semaforoFosforo.release()
        if caso == 2:
            fosforosEnMesa = True
            tabacoEnMesa = True
            semaforoFosforo.release()
            semaforoTabaco.release()
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    while True:
        semaforoTabaco.acquire()
        semaforoFosforo.acquire()
        if (fosforosEnMesa and tabacoEnMesa):
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador1 con papel - tengo fosforo y tabaco en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()

def fumadorConFosforos():
    while True:
        semaforoPapel.acquire()
        semaforoTabaco.acquire()
        if (papelEnMesa and tabacoEnMesa):
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador2 con fosforo - tengo tabaco y papel en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()

def fumadorConTabaco():
    while True:
        semaforoFosforo.acquire()
        semaforoPapel.acquire()
        if (fosforosEnMesa and papelEnMesa):
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador3 con tabaco - tengo papel y fosforo en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

