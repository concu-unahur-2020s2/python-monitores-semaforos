import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False


semaforoAgente = threading.Semaphore(1)


def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    ingredientesEnMesa = 6
    while True:
        while ingredientesEnMesa >= 0:
            semaforoAgente.acquire()
            caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
            if caso == 0:
                papelEnMesa = True
                tabacoEnMesa = True
            if caso == 1:
                papelEnMesa = True
                fosforosEnMesa = True
            if caso == 2:
                fosforosEnMesa = True
                tabacoEnMesa = True
            ingredientesEnMesa -=1
          
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while fosforosEnMesa == True and tabacoEnMesa == True: # si hay fósforos y tabaco en la mesa
            fosforosEnMesa = False 
            tabacoEnMesa = False # tomarlos
            print("fumadorConPapel fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while papelEnMesa == True and tabacoEnMesa == True: # si hay papel y tabaco en la mesa
            papelEnMesa = False  
            tabacoEnMesa = False # tomarlos
            print("fumadorConFosforos fumando 🚬 ") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while fosforosEnMesa == True and papelEnMesa == True: # si hay fósforos y papel en la mesa
            fosforosEnMesa = False 
            papelEnMesa = False # tomarlos
            print("fumadorConTabaco fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
            semaforoAgente.release() # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()