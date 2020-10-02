import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

semaforoAgente = threading.Semaphore(1)

def agente1():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa = True
        tabacoEnMesa = True

def agente2():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa = True
        fosforosEnMesa = True

def agente3():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        fosforosEnMesa = True
        tabacoEnMesa = True

def fumadorConPapel():
    while True:
        while (fosforosEnMesa and tabacoEnMesa):
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador1 con papel - tengo fosforo y tabaco en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()

def fumadorConFosforos():
    while True:
        while (papelEnMesa and tabacoEnMesa):
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador2 con fosforo - tengo tabaco y papel en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()

def fumadorConTabaco():
    while True:
        while (fosforosEnMesa and papelEnMesa):
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
            print("fumador3 con tabaco - tengo papel y fosforo en la mesa - voy a fumar")
            time.sleep(2)
        semaforoAgente.release()


agenteHilo1 = threading.Thread(target=agente1)
agenteHilo2 = threading.Thread(target=agente2)
agenteHilo3 = threading.Thread(target=agente3)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo1.start()
agenteHilo2.start()
agenteHilo3.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
