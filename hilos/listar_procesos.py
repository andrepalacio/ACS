import psutil
import os

def listar_procesos():
    for proceso in psutil.process_iter(attrs=['pid', 'name']):
        print(proceso.info)

def eliminar_proceso(pid):
    try:
        os.kill(pid, 9)
        print(f"Proceso {pid} eliminado")
    except Exception as e:
        print(f"Error eliminando proceso: {e}")

listar_procesos()
pid = int(input("Ingrese el PID a eliminar: "))
eliminar_proceso(pid)
