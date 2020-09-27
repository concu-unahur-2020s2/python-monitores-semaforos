import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def armadorConPapel():
     global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        print("Voy armar con papel")
        for i in range(5):
            with monitor:
                papelEnMesa = True
                tabacoEnMesa = True
                cigarrillosSinFumar.append(i)
                monitor.notify_all()
                time.sleep(1)

def armadorConFosforos():
     global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        print("Voy armar con fosforos")
        for i in range(5):
            with monitor:
                papelEnMesa = True
                fosforosEnMesa = True
                cigarrillosSinFumar.append(i)
                monitor.notify_all()
                time.sleep(1)

def armadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        print("Voy armar con tabaco")
        for i in range(5):
            with monitor: 
                fosforosEnMesa = True
                tabacoEnMesa = True
                cigarrillosSinFumar.append(i)
                monitor.notify_all()
                time.sleep(1)
           
def fumador():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        while fosforosEnMesa == True and tabacoEnMesa == True: # si hay fósforos y tabaco en la mesa
            fosforosEnMesa = False 
            tabacoEnMesa = False # tomarlos
            print("fumador fumando 🚬") 
            time.sleep(2) # armar cigarrillo y fumar: se puede simular con un sleep
    



cigarrillosSinFumar = []

cigarrillosSinFumar_monit = threading.Condition()

fumadorHilo = threading.Thread(target=fumador)
armadorConPapelHilo = threading.Thread(target=armadorConPapel)
armadorConFosforosHilo = threading.Thread(target=armadorConFosforos)
armadorConTabacoHilo = threading.Thread(target= armadorConTabaco)

fumadorHilo.start()
armadorConPapelHilo.start()
armadorConFosforosHilo.start()
armadorConTabacoHilo.start()