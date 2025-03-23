import threading

def generar_secuencia(n1, n2):
    if n1 < n2:
        print(f"Secuencia: {list(range(n1, n2+1))}")

n1, n2 = 5, 10
hilo = threading.Thread(target=generar_secuencia, args=(n1, n2))
hilo.start()
hilo.join()

print(f"Resta: {n2 - n1}")
