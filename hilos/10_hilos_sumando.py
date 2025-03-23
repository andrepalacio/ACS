import threading
import random

resultados = []
lock = threading.Lock()

def calcular_suma(index):
    suma = sum(random.randint(1, 1000) for _ in range(100))
    with lock:
        resultados.append((index, suma))

hilos = []
for i in range(10):
    hilo = threading.Thread(target=calcular_suma, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

ganador = max(resultados, key=lambda x: x[1])
print(f"Hilo ganador: {ganador[0]} con suma {ganador[1]}")