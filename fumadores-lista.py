import random
import threading
import time

papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        caso = random.choice([0,1,2])
        if caso == 0:
            papelEnMesa.append(1)
            tabacoEnMesa.append(1)
            print("\nEl agente coloco papel y tabaco.")
        if caso == 1:
            papelEnMesa.append(1)
            fosforosEnMesa.append(1)
            print("\nEl agente coloco papel y fosforos.")
        if caso == 2:
            fosforosEnMesa.append(1)
            tabacoEnMesa.append(1)
            print("\nEl agente coloco fosforos y tabaco.")
        time.sleep(1)

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(fosforosEnMesa) == 1 and len(tabacoEnMesa) == 1:
            fosforosEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Fumador con papel esta fumando 🚬")
            time.sleep(2)
            semaforoAgente.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) == 1 and len(tabacoEnMesa) == 1:
            papelEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Fumador con fosforos esta fumando 🚬")
            time.sleep(2)
            semaforoAgente.release()

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) == 1 and len(fosforosEnMesa) == 1:
            papelEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            print("Fumador con tabaco esta fumando 🚬")
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
