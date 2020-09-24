import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papelEnMesa = True
            tabacoEnMesa = True
            print("\nEl agente coloco papel y tabaco.")
        if caso == 1:
            papelEnMesa = True
            fosforosEnMesa = True
            print("\nEl agente coloco papel y fosforos.")
        if caso == 2:
            fosforosEnMesa = True
            tabacoEnMesa = True
            print("\nEl agente coloco fosforos y tabaco.")
        time.sleep(1)
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
        if fosforosEnMesa == True and tabacoEnMesa == True:
            fosforosEnMesa = False
            tabacoEnMesa = False
            print("Fumador con papel esta fumando...")
            time.sleep(2)
            semaforoAgente.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
        if papelEnMesa == True and tabacoEnMesa == True:
            papelEnMesa = False
            tabacoEnMesa = False
            print("Fumador con fosforos esta fumando...")
            time.sleep(2)
            semaforoAgente.release()

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
        if papelEnMesa == True and fosforosEnMesa == True:
            papelEnMesa = False
            fosforosEnMesa = False
            print("Fumador con tabaco esta fumando...")
            time.sleep(2)
            semaforoAgente.release()


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

semaforoAgente = threading.Semaphore(1)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
