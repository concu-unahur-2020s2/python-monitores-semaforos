import random
import threading
import time

listaPapel = []
listaTabaco = []
listaFosforo = []
listaCicarrito = []


def agente():
    while True:
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            listaPapel.append(1)
            listaTabaco.append(1)
        if caso == 1:
            listaPapel.append(1)
            listaFosforo.append(1)
        if caso == 2:
            listaFosforo.append(1)
            listaTabaco.append(1)
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def armadorConPapel():
    while True:
        if (len(listaFosforo) > 0 and len(listaTabaco) > 0):
            listaCicarrito.append(1)
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("armador1 con papel - armo un cigarrito")
            time.sleep(2)


def armadorConFosforos():
    while True:
        if (len(listaPapel) > 0 and len(listaTabaco) > 0):
            listaCicarrito.append(1)
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("armador2 con fosforo - armo un cigarrito")
            time.sleep(2)


def armadorConTabaco():
    while True:
        if (len(listaFosforo) > 0 and len(listaPapel) > 0):
            listaCicarrito.append(1)
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("armador3 con tabaco - armo un cigarrito")
            time.sleep(2)

def fumador():
    while True:
        if (len(listaCicarrito) > 0):
            listaCicarrito.pop(0)
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("me fumo uno, quedan", len(listaCicarrito), "en la mesa")
            time.sleep(2)    


agenteHilo = threading.Thread(target=agente)
armadorConPapelHilo = threading.Thread(target=armadorConPapel)
armadorConFosforosHilo = threading.Thread(target=armadorConFosforos)
armadorConTabacoHilo = threading.Thread(target=armadorConTabaco)
fumadorHilo = threading.Thread(target=fumador)

agenteHilo.start()
armadorConPapelHilo.start()
armadorConFosforosHilo.start()
armadorConTabacoHilo.start()
fumadorHilo.start()