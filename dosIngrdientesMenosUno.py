import random
import threading
import time

semaforoAgente = threading.Semaphore(2)
semaforoListas = threading.Lock()

def agenteA():   
    while True:
        semaforoAgente.acquire()
        restante = "El agente A coloco:"
        semaforoListas.acquire()
        if len(papelEnMesa) < 2:
            papelEnMesa.append(1)
            restante += "papel,"
        if len(tabacoEnMesa) < 2:
            tabacoEnMesa.append(1)
            restante += "tabaco,"
        semaforoListas.release()
        print("\n" + restante)
        time.sleep(1)

def agenteB():
    while True:
        semaforoAgente.acquire()
        restante = "El agente B coloco:"
        semaforoListas.acquire()
        if len(papelEnMesa) < 2:
            papelEnMesa.append(1)
            restante += "papel,"
        if len(fosforosEnMesa) < 1:
            fosforosEnMesa.append(1)
            restante += "fosforo,"
        semaforoListas.release()
        print("\n" + restante)
        time.sleep(1)

def agenteC():
    while True:
        semaforoAgente.acquire()
        restante = "El agente C coloco:"
        semaforoListas.acquire()
        if len(fosforosEnMesa) < 1:
            fosforosEnMesa.append(1)
            restante += "fosforo,"
        if len(tabacoEnMesa) < 2:
            tabacoEnMesa.append(1)
            restante += "tabaco,"
        semaforoListas.release()
        print("\n" + restante)
        time.sleep(1)

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        while len(fosforosEnMesa) >= 1 and len(tabacoEnMesa) >= 1: 
            fosforosEnMesa.pop(0) 
            tabacoEnMesa.pop(0)
            print("fumadorConPapel fumando 🚬") 
            time.sleep(2) 
            semaforoAgente.release() 
        semaforoListas.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        while len(papelEnMesa) >= 1 and len(tabacoEnMesa) >= 1 : # si hay papel y tabaco en la mesa
            papelEnMesa.pop(0) 
            tabacoEnMesa.pop(0) # tomarlos
            print("fumadorConFosforos fumando 🚬 ") 
            time.sleep(2) 
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
        semaforoListas.release()

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        while len(fosforosEnMesa) >=1 and len(papelEnMesa) >= 1: # si hay fósforos y papel en la mesa
            fosforosEnMesa.pop(0) 
            papelEnMesa.pop(0) # tomarlos
            print("fumadorConTabaco fumando 🚬") 
            time.sleep(2) 
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar
        semaforoListas.release()

papelEnMesa = []
tabacoEnMesa = []
fosforosEnMesa = []

agenteAHilo = threading.Thread(target=agenteA)
agenteBHilo = threading.Thread(target=agenteB)
agenteCHilo = threading.Thread(target=agenteC)

fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteAHilo.start()
agenteBHilo.start()
agenteCHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()