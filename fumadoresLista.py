import logging
import threading
import time
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

n = 2

semaforoAgente = threading.Semaphore(0)
semaforoFumadorConFosforos = threading.Semaphore(0)
semaforoFumadorConTabaco = threading.Semaphore(0)
semaforoFumadorConPapel = threading.Semaphore(0)

listaFosforo = []
listaTabaco = []
listaPapel = []


def agente():
    while True:
        caso = random.choice([0, 1, 2])
        if caso == 0:
            logging.info('Puse papel y tabaco...')
            listaPapel.append(0)
            listaTabaco.append(1)
            time.sleep(n)
            semaforoFumadorConFosforos.release()
        if caso == 1:
            logging.info('Puse papel y fósforos...')
            listaPapel.append(0)
            listaFosforo.append(2)
            time.sleep(n)
            semaforoFumadorConTabaco.release()
        if caso == 2:
            logging.info('Puse fósforos y tabaco...')
            listaTabaco.append(1)
            listaFosforo.append(2)
            time.sleep(n)
            semaforoFumadorConPapel.release()
        semaforoAgente.acquire()


def fumadorConPapel():
    while True:
        if len(listaPapel) > 0:
            semaforoFumadorConPapel.acquire()
            logging.info('Armando cigarrillo...')
            listaFosforo.pop()
            listaTabaco.pop()
            time.sleep(n)
            logging.info('Fumando cigarrillo...')
            time.sleep(n)
        semaforoAgente.release()


def fumadorConFosforos():
            if len(listaFosforo) > 0:
                semaforoFumadorConFosforos.acquire()
                logging.info('Armando cigarrillo...')
                listaPapel.pop()
                listaTabaco.pop()
                time.sleep(n)
                logging.info('Fumando cigarrillo...')
                time.sleep(n)
                semaforoAgente.release()


def fumadorConTabaco():
    while True:
        if len(listaTabaco) > 0:
            semaforoFumadorConTabaco.acquire()
            logging.info('Armando cigarrillo...')
            listaPapel.pop()
            listaFosforo.pop()
            time.sleep(n)
            logging.info('Fumando cigarrillo...')
            time.sleep(n)
            semaforoAgente.release()


agente = threading.Thread(target=agente, name='Agente')
fumadorConPapel = threading.Thread(target=fumadorConPapel, name='Fumador con papel')
fumadorConFosforos = threading.Thread(target=fumadorConFosforos, name='Fumador con fósforos')
fumadorConTabaco = threading.Thread(target=fumadorConTabaco, name='Fumador con tabaco')

agente.start()
fumadorConPapel.start()
fumadorConFosforos.start()
fumadorConTabaco.start()
