import threading
import random
import time

lista = []
lock = threading.Lock()  # Para evitar condiciones de carrera
stop_event = threading.Event()  # Para detener los hilos

def generar_numeros():
    """Genera números aleatorios entre 1 y 100 y los inserta en la lista."""
    while not stop_event.is_set():
        num = random.randint(1, 100)
        with lock:
            lista.append(num)
        time.sleep(0.01)  # Pequeña pausa para simular procesamiento

def modificar_lista():
    """Recorre la lista y sustituye los números terminados en 0 por -1."""
    index = 0
    while not stop_event.is_set():
        with lock:
            if lista and lista[index % len(lista)] % 10 == 0:
                lista[index % len(lista)] = -1
        index += 1
        time.sleep(0.01)  # Pequeña pausa para evitar sobrecarga

def verificar_suma():
    """Aborta los otros dos hilos cuando la suma supera 20000."""
    while not stop_event.is_set():
        with lock:
            if sum(lista) > 20000:
                print("🔴 Deteniendo hilos, la suma superó 20000")
                stop_event.set()
        time.sleep(0.1)  # Verifica cada 100ms

# Crear hilos
hilo1 = threading.Thread(target=generar_numeros, name="Generador")
hilo2 = threading.Thread(target=modificar_lista, name="Modificador")
hilo3 = threading.Thread(target=verificar_suma, name="Verificador")

# Iniciar hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar la finalización del tercer hilo (que detendrá a los otros)
hilo3.join()

print("✅ Programa terminado.")