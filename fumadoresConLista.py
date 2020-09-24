import random
import threading
import time



semaforoAgente = threading.Semaphore(1)

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            papelEnMesa.append("blanco")
            tabacoEnMesa.append("Richtmon")
        if caso == 1:
            papelEnMesa.append("negro")
            fosforosEnMesa.append ("3 patitos")
        if caso == 2:
            fosforosEnMesa.append("fragata")
            tabacoEnMesa.append("Particulares")
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(fosforosEnMesa) != 0 and len(tabacoEnMesa) != 0: # si hay fósforos y tabaco en la mesa
            fosforosEnMesa.pop(0) 
            tabacoEnMesa.pop(0) # tomarlos
            print("fumadorConPapel fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(papelEnMesa) != 0 and len(tabacoEnMesa) != 0 : # si hay papel y tabaco en la mesa
            papelEnMesa.pop(0) 
            tabacoEnMesa.pop(0) # tomarlos
            print("fumadorConFosforos fumando 🚬 ") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(fosforosEnMesa) !=0 and len(papelEnMesa) != 0: # si hay fósforos y papel en la mesa
            fosforosEnMesa.pop(0) 
            tabacoEnMesa.pop(0) # tomarlos
            print("fumadorConTabaco fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


papelEnMesa = []
tabacoEnMesa = []
fosforosEnMesa = []

agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

