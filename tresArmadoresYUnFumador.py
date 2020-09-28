import random
import threading
import time

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def armadorConPapel(monitor):
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

def armadorConFosforos(monitor):
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

def armadorConTabaco(monitor):
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
           
class Fumador(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self):
        while (True):
            with self.monitor:         
                while len(cigarrillosSinFumar)<1:    
                    self.monitor.wait()  
                x = cigarrillosSinFumar.pop(0) 
                print("fumador fumando 🚬") 
                time.sleep(2) 
    



cigarrillosSinFumar = []

cigarrillosSinFumar_monit = threading.Condition()

fumadorA = Fumador(cigarrillosSinFumar_monit)
fumadorA.start()

armadorConFosforos(cigarrillosSinFumar_monit)
armadorConPapel(cigarrillosSinFumar_monit)
armadorConTabaco(cigarrillosSinFumar_monit)


