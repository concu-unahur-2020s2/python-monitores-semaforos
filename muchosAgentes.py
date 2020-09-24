import random
import threading
import time

semaforoAgente = threading.Semaphore(1)

def agentePapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append("blanco")
        tabacoEnMesa.append("Richtmon")
        
def agenteFosforo():
    global papelEnMesa,fosforosEnMesa,tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        papelEnMesa.append("negro")
        fosforosEnMesa.append ("3 patitos")

def agenteTabaco():
    global papelEnMesa,fosforosEnMesa,tabacoEnMesa
    while True:
        semaforoAgente.acquire()    
        fosforosEnMesa.append("fragata")
        tabacoEnMesa.append("Particulares")
       

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
            papelEnMesa.pop(0) # tomarlos
            print("fumadorConTabaco fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


papelEnMesa = []
tabacoEnMesa = []
fosforosEnMesa = []

agenteFosforo = threading.Thread(target=agenteFosforo)
agentePapel = threading.Thread(target=agentePapel)
agenteTabaco = threading.Thread(target=agenteTabaco)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteFosforo.start()
agentePapel.start()
agenteTabaco.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()