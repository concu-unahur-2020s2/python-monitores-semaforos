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
            papelEnMesa.append(1)
            tabacoEnMesa.append(1)
        if caso == 1:
            papelEnMesa.append(1)
            fosforosEnMesa.append(1)
        if caso == 2:
            fosforosEnMesa.append(1)
            tabacoEnMesa.append(1)

def armadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(fosforosEnMesa) >=1 and len(tabacoEnMesa) >=1:
            print("Voy armar con papel")
            tabacoEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            cigarrillosSinFumar.append("🚬")
            time.sleep(2)
            semaforoAgente.release()

def armadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(papelEnMesa) >=1 and len(tabacoEnMesa) >=1:
            print("Voy armar con fosforo")
            papelEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            cigarrillosSinFumar.append("🚬")
            time.sleep(2)
            semaforoAgente.release()
 
def armadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(papelEnMesa) >=1 and len(fosforosEnMesa) >=1:
            print("Voy armar con tabaco")
            papelEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            cigarrillosSinFumar.append("🚬")
            time.sleep(2)
            semaforoAgente.release()

def fumador():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while len(cigarrillosSinFumar) > 0:
            cigarrillosSinFumar.pop(0)
            print("Fumando 🚬 Me quedan sin fumar:" + str(len(cigarrillosSinFumar)))
            time.sleep(4)


papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []

cigarrillosSinFumar = []

agenteHilo = threading.Thread(target= agente)

armadorConFosforosHilo = threading.Thread(target= armadorConFosforos)
armadorConPapelHilo = threading.Thread(target= armadorConPapel)
armadorConTabacoHilo = threading.Thread(target= armadorConTabaco)

fumadorHilo = threading.Thread(target= fumador)

agenteHilo.start()
armadorConFosforosHilo.start()
armadorConPapelHilo.start()
armadorConTabacoHilo.start()
fumadorHilo.start()

