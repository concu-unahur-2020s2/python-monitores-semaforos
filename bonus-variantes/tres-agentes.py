import random
import threading
import time

papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []

def agente0():
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append(1)
        tabacoEnMesa.append(1)
        print("\nEl agente 0 coloco papel y tabaco.")
        time.sleep(1)

def agente1():
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append(1)
        fosforosEnMesa.append(1)
        print("\nEl agente 1 coloco papel y fosforos.")
        time.sleep(1)

def agente2():
    while True:
        semaforoAgente.acquire()
        fosforosEnMesa.append(1)
        tabacoEnMesa.append(1)
        print("\nEl agente 2 coloco fosforos y tabaco.")



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


agente0 = threading.Thread(target=agente0)
agente1 = threading.Thread(target=agente1)
agente2 = threading.Thread(target=agente2)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

semaforoAgente = threading.Semaphore(1)

agente0.start()
agente1.start()
agente2.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
