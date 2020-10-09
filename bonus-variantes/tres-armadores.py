import random
import threading
import time

papelEnMesa = []
fosforosEnMesa = []
tabacoEnMesa = []
cigarrosArmados = []

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        semaforoAgente.acquire()
        for i in range(2):
            caso = random.choice([0,1,2])
            if caso == 0:
                papelEnMesa.append(i)
                tabacoEnMesa.append(i)
                print("\nEl agente coloco papel y tabaco.")
            if caso == 1:
                papelEnMesa.append(i)
                fosforosEnMesa.append(i)
                print("\nEl agente coloco papel y fosforos.")
            if caso == 2:
                fosforosEnMesa.append(i)
                tabacoEnMesa.append(i)
                print("\nEl agente coloco fosforos y tabaco.")
            time.sleep(1)

def armadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(fosforosEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            fosforosEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Armador con papel esta armando un cigarro.")
            time.sleep(2)
            cigarrosArmados.append("🚬")
            semaforoAgente.release()


def armadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) >= 1 and len(tabacoEnMesa) >= 1:
            papelEnMesa.pop(0)
            tabacoEnMesa.pop(0)
            print("Armador con fosforos esta armando un cigarro.")
            time.sleep(2)
            cigarrosArmados.append("🚬")
            semaforoAgente.release()

def armadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(papelEnMesa) >= 1 and len(fosforosEnMesa) >= 1:
            papelEnMesa.pop(0)
            fosforosEnMesa.pop(0)
            print("Armador con tabaco esta armando un cigarro.")
            time.sleep(2)
            cigarrosArmados.append("🚬")
            semaforoAgente.release()

def fumador():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        if len(cigarrosArmados) > 0:
            cigarrosArmados.pop(0)
            print("\n - - - - - - - - - - - - - - \n")
            print("Fumando 🚬 [Restantes: " + str(len(cigarrosArmados)) + "]")
            print("\n - - - - - - - - - - - - - - \n")
            time.sleep(4)


agenteHilo = threading.Thread(target=agente)
armadorConPapelHilo = threading.Thread(target=armadorConPapel)
armadorConFosforosHilo = threading.Thread(target=armadorConFosforos)
armadorConTabacoHilo = threading.Thread(target=armadorConTabaco)
fumador = threading.Thread(target=fumador)

semaforoAgente = threading.Semaphore(1)

agenteHilo.start()
armadorConPapelHilo.start()
armadorConFosforosHilo.start()
armadorConTabacoHilo.start()
fumador.start()