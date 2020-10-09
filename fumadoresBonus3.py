import random
import threading
import time

listaPapel = []
listaTabaco = []
listaFosforo = []

semaforoPapel = threading.Semaphore(2)
semaforoTabaco = threading.Semaphore(2)
semaforoFosforo = threading.Semaphore(2)

def agente():
    while True:
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            semaforoPapel.acquire()
            listaPapel.append(1)
            semaforoTabaco.acquire()
            listaTabaco.append(1)
        if caso == 1:
            semaforoPapel.acquire()
            listaPapel.append(1)
            semaforoFosforo.acquire()
            listaFosforo.append(1)
        if caso == 2:
            semaforoFosforo.acquire()
            listaFosforo.append(1)
            semaforoTabaco.acquire()
            listaTabaco.append(1)
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    while True:
        if (len(listaFosforo) > 0 and len(listaTabaco) > 0):
            semaforoFosforo.release()
            listaFosforo.pop(0)
            semaforoTabaco.release()
            listaTabaco.pop(0)
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador1 con papel - tengo fosforo y tabaco en la mesa - voy a fumar")
            time.sleep(2)


def fumadorConFosforos():
    while True:
        if (len(listaPapel) > 0 and len(listaTabaco) > 0):
            semaforoPapel.release()
            listaPapel.pop(0)
            semaforoTabaco.release()
            listaTabaco.pop(0)
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador2 con fosforo - tengo tabaco y papel en la mesa - voy a fumar")
            time.sleep(2)


def fumadorConTabaco():
    while True:
        if (len(listaFosforo) > 0 and len(listaPapel) > 0):
            semaforoFosforo.release()
            listaFosforo.pop(0)
            semaforoPapel.release()
            listaPapel.pop(0)
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador3 con tabaco - tengo papel y fosforo en la mesa - voy a fumar")
            time.sleep(2)



agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()