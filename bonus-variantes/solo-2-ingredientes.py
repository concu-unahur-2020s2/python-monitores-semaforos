import random
import threading
import time

papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []

def agente0():
    while True:
        semaforoAgente.acquire()
        res = "El agente 0 coloco"

        semaforoListas.acquire()
        if len(papelEnMesa) < 2:
            papelEnMesa.append(1)
            res += " papel,"
        if len(tabacoEnMesa) < 2:
            tabacoEnMesa.append(1)
            res += " tabaco,"
        semaforoListas.release()

        print("\n" + res)
        time.sleep(1)

def agente1():
    while True:
        semaforoAgente.acquire()
        res = "El agente 1 coloco"

        semaforoListas.acquire()
        if len(papelEnMesa) < 2:
            papelEnMesa.append(1)
            res += " papel,"
        if len(fosforosEnMesa) < 2:
            fosforosEnMesa.append(1)
            res += " fosforos,"
        semaforoListas.release()

        print("\n" + res)
        time.sleep(1)

def agente2():
    while True:
        semaforoAgente.acquire()
        res = "El agente 2 coloco"

        semaforoListas.acquire()
        if len(fosforosEnMesa) < 2:
            fosforosEnMesa.append(1)
            res += " fosforos,"
        if len(tabacoEnMesa) < 2:
            tabacoEnMesa.append(1)
            res += " tabaco,"
        semaforoListas.release()

        print("\n" + res)
        time.sleep(1)


def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        if len(fosforosEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            fosforosEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Fumador con papel esta fumando 🚬")
            time.sleep(2)
            semaforoAgente.release()
        semaforoListas.release()


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        if len(papelEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            papelEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Fumador con fosforos esta fumando 🚬")
            time.sleep(2)
            semaforoAgente.release()
        semaforoListas.release()

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoListas.acquire()
        if len(papelEnMesa) >= 1 and len(fosforosEnMesa) >= 1:
            papelEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            print("Fumador con tabaco esta fumando 🚬")
            time.sleep(2)
            semaforoAgente.release()
        semaforoListas.release()


agente0 = threading.Thread(target=agente0)
agente1 = threading.Thread(target=agente1)
agente2 = threading.Thread(target=agente2)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

semaforoAgente = threading.Semaphore(2)
semaforoListas = threading.Lock()

agente0.start()
agente1.start()
agente2.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()
