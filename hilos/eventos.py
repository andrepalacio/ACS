import threading
import time

def genera_eventos():
    for _ in range(5):
        time.sleep(2)
        ev.set()  
    stop_event.set()  # Indica que debe finalizar el programa

def escribe_algo():     
    while not stop_event.is_set():  # Verifica si debe terminar
        ev.wait()
        if stop_event.is_set():
            break  # Sale del bucle si la señal de parada está activa
        print("hola")
        ev.clear()

ev = threading.Event()
stop_event = threading.Event()  # Nueva señal para detener el hilo

T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()

T1.join()
T2.join()  # Asegura que el programa termine correctamente
