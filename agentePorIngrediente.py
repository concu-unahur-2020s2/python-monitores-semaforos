import random
import threading
import time

semaforoAgente = threading.Semaphore(2)

def agentePapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append(1)
        print("coloco papel")
        time.sleep(1)

def agenteFosforo():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        fosforosEnMesa.append(1)
        print("coloco fosforo")
        time.sleep(1)

def agenteTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        tabacoEnMesa.append(1)
        print("coloco tabaco")
        time.sleep(1)

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(fosforosEnMesa) >= 1 and len(tabacoEnMesa) >= 1: 
            fosforosEnMesa.pop(0) 
            tabacoEnMesa.pop(0) 
            print("fumadorConPapel fumando 🚬") 
            time.sleep(2) 
            semaforoAgente.release()
            semaforoAgente.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(papelEnMesa) >= 1 and len(tabacoEnMesa) >= 1 : 
            papelEnMesa.pop(0) 
            tabacoEnMesa.pop(0) 
            print("fumadorConFosforos fumando 🚬 ") 
            time.sleep(2) 
            semaforoAgente.release() 
            semaforoAgente.release()

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(fosforosEnMesa) >=1 and len(papelEnMesa) >= 1: 
            fosforosEnMesa.pop(0) 
            papelEnMesa.pop(0) 
            print("fumadorConTabaco fumando 🚬") 
            time.sleep(2) 
            semaforoAgente.release() 
            semaforoAgente.release()


papelEnMesa = []
tabacoEnMesa = []
fosforosEnMesa = []

agentePapelHilo = threading.Thread(target=agentePapel)
agenteFosforoHilo = threading.Thread(target = agenteFosforo)
agenteTabacoHilo = threading.Thread(target=agenteTabaco)

fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agentePapelHilo.start()
agenteFosforoHilo.start()
agenteTabacoHilo.start()

fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()