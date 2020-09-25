import random
import threading
import time

papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []

def agentePapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append(1)
        print("Coloco Papel")
        time.sleep(1)

def agenteTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        tabacoEnMesa.append(1)
        print("Coloco Tabaco")
        time.sleep(1)

def agenteFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        fosforosEnMesa.append(1)
        print("Coloco Fosforos")
        time.sleep(1)


def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(fosforosEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            fosforosEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("\nFumador con papel esta fumando 🚬\n")
            time.sleep(2)
            semaforoAgente.release()
            semaforoAgente.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            papelEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("\nFumador con fosforos esta fumando 🚬\n")
            time.sleep(2)
            semaforoAgente.release()
            semaforoAgente.release()


def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) >= 1 and len(fosforosEnMesa) >= 1:
            papelEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            print("\nFumador con tabaco esta fumando 🚬\n")
            time.sleep(2)
            semaforoAgente.release()
            semaforoAgente.release()


agentePapel = threading.Thread(target=agentePapel)
agenteTabaco = threading.Thread(target=agenteTabaco)
agenteFosforos = threading.Thread(target=agenteFosforos)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

semaforoAgente = threading.Semaphore(2)

agentePapel.start()
agenteTabaco.start()
agenteFosforos.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
