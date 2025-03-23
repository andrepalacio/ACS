import threading

def calcular_area_rectangulo(base, altura, resultado, index):
    resultado[index] = base * altura

def calcular_area_triangulo(base, altura, resultado, index):
    resultado[index] = (base * altura) / 2

areas = [0, 0]  # Almacenará los resultados

hilo1 = threading.Thread(target=calcular_area_rectangulo, args=(10, 5, areas, 0))
hilo2 = threading.Thread(target=calcular_area_triangulo, args=(6, 4, areas, 1))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

area_total = sum(areas)
print(f"Área total: {area_total}")
