import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s')

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class HiloProductor(threading.Thread):
    def __init__(self, name=None):
        super(HiloProductor, self).__init__()
        self.name = name

    def run(self):
        while True:
            item = random.randint(1, 10)
            q.put(item)  # Bloquea si la cola está llena
            logging.debug(f'Insertando "{item}" : {q.qsize()} elementos en la cola')
            time.sleep(random.random())

class HiloConsumidor(threading.Thread):
    def __init__(self, name=None):
        super(HiloConsumidor, self).__init__()
        self.name = name

    def run(self):
        while True:
            item = q.get()  # Bloquea si la cola está vacía
            logging.debug(f'Sacando "{item}" : {q.qsize()} elementos en la cola')
            time.sleep(random.random())
            q.task_done()  # Indica que el ítem fue procesado

# Crear y lanzar hilos
p1 = HiloProductor(name='Productor1')
p2 = HiloProductor(name='Productor2')
c1 = HiloConsumidor(name='Consumidor1')

p1.start()
p2.start()
c1.start()

# Esperar a que la cola se vacíe
q.join()

# Detener los hilos

p1.join()
p2.join()
c1.join()