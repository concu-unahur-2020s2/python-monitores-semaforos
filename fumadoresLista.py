import random
import threading
import time
papel = []
tabaco = []
fosforo = []

def agente():
    while True:
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papel.append(1)
            tabaco.append(1)
        if caso == 1:
            papel.append(1)
            fosforo.append(1)
        if caso == 2:
            fosforo.append(1)
            tabaco.append(1)
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    while True:
        if (len(fosforo) > 0 and len(tabaco) > 0):
            fosforo.pop(0)
            tabaco.pop(0)
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumar")
            time.sleep(2)


def fumadorConFosforos():
    while True:
        if (len(papel) > 0 and len(tabaco) > 0):
            papel.pop(0)
            tabaco.pop(0)
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumar")
            time.sleep(2)


def fumadorConTabaco():
    while True:
        if (len(fosforo) > 0 and len(papel) > 0):
            fosforo.pop(0)
            papel.pop(0)
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumar")
            time.sleep(2)



agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()