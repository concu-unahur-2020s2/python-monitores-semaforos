import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

n = 2

semaforoAgente = threading.Semaphore(0)
semaforoFumadorConFosforos = threading.Semaphore(0)
semaforoFumadorConTabaco = threading.Semaphore(0)
semaforoFumadorConPapel = threading.Semaphore(0)


def agente():
    while True:
        caso = random.choice([0, 1, 2])
        if caso == 0:
            logging.info('Puse papel y tabaco...')
            time.sleep(n)
            semaforoFumadorConFosforos.release()

        if caso == 1:
            logging.info('Puse papel y fósforos...')
            time.sleep(n)
            semaforoFumadorConTabaco.release()

        if caso == 2:
            logging.info('Puse fósforos y tabaco...')
            time.sleep(n)
            semaforoFumadorConPapel.release()
        semaforoAgente.acquire()


def fumadorConPapel():
    while True:
        semaforoFumadorConPapel.acquire()
        logging.info('Armando cigarrillo...')
        time.sleep(n)
        logging.info('Fumando cigarrillo...')
        time.sleep(n)
        semaforoAgente.release()


def fumadorConFosforos():
    while True:
        semaforoFumadorConFosforos.acquire()
        logging.info('Armando cigarrillo...')
        time.sleep(n)
        logging.info('Fumando cigarrillo...')
        time.sleep(n)
        semaforoAgente.release()


def fumadorConTabaco():
    while True:
        semaforoFumadorConTabaco.acquire()
        logging.info('Armando cigarrillo...')
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
