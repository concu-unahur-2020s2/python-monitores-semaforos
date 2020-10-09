import random
import threading
import time

listaPapel = []
listaTabaco = []
listaFosforo = []

semaforoAgente = threading.Semaphore(2)

class Agente(threading.Thread):
    def __init__(self,lista,semaforo,nro):
        super().__init__()
        self.lista = lista
        self.semaforo = semaforo
        self.nro = nro

    def run(self):
        while True:
            self.semaforo.acquire()
            self.lista.append(1)
            print("agente",self.nro, "cantidad", len(self.lista))
            time.sleep(2)


class Fumador(threading.Thread):
    def __init__(self,lista1, lista2, semaforo,nro):
        super().__init__()
        self.lista1 = lista1
        self.lista2 = lista2
        self.semaforo = semaforo
        self.nro = nro

    def run(self):
        while True:
            if(len(self.lista1) > 0 and len(self.lista2) > 0):
                self.lista1.pop(0)
                self.lista2.pop(0)
                print("fumador",self.nro, "voy a fumar")
                time.sleep(2)
                self.semaforo.release()
                self.semaforo.release()



agente1 = Agente(listaFosforo,semaforoAgente,1)
agente2 = Agente(listaPapel,semaforoAgente,2)
agente3 = Agente(listaTabaco,semaforoAgente,3)

fumadorConFosforos = Fumador(listaTabaco,listaPapel,semaforoAgente,1)
fumadorConPapel = Fumador(listaFosforo,listaTabaco,semaforoAgente,2)
fumadorConTabaco = Fumador(listaFosforo,listaPapel,semaforoAgente,3)


agente1.start()
agente2.start()
agente3.start()
fumadorConPapel.start()
fumadorConFosforos.start()
fumadorConTabaco.start()