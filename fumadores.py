import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
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
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


def fumadorConFosforos():
    while True:
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def fumadorConTabaco():
    while True:
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

