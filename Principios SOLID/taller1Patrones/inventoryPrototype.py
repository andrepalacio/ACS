from abc import ABC, abstractmethod
import copy

# --- Ejercicio 3: Control de Inventario (Prototype + Strategy) ---
class InventoryAlgorithm(ABC):
    @abstractmethod
    def optimize(self, stock):
        pass

class FIFOInventory(InventoryAlgorithm):
    def optimize(self, stock):
        return sorted(stock, key=lambda x: x['fecha_ingreso'])

class LIFOInventory(InventoryAlgorithm):
    def optimize(self, stock):
        return sorted(stock, key=lambda x: x['fecha_ingreso'], reverse=True)

class JITInventory(InventoryAlgorithm):
    def optimize(self, stock):
        return [item for item in stock if item['demandado']]

class InventoryManager:
    def __init__(self):
        self.algorithms = {}
        self.current_strategy = None

    def agregar_algoritmo(self, name, algorithm: InventoryAlgorithm):
        self.algorithms[name] = algorithm

    def eliminar_algoritmo(self, name):
        if name in self.algorithms:
            del self.algorithms[name]

    def editar_algoritmo(self, name, new_algorithm: InventoryAlgorithm):
        if name in self.algorithms:
            self.algorithms[name] = new_algorithm

    def set_strategy(self, name):
        if name in self.algorithms:
            self.current_strategy = self.algorithms[name]

    def optimize_inventory(self, stock):
        if self.current_strategy:
            return self.current_strategy.optimize(stock)
        else:
            raise ValueError("No se ha seleccionado una estrategia")

    def clone_version(self):
        return copy.deepcopy(self)

# --- Pruebas ---
if __name__ == "__main__":
    stock = [
        {"producto": "A", "fecha_ingreso": "2024-01-01", "demandado": True},
        {"producto": "B", "fecha_ingreso": "2024-02-01", "demandado": False}
    ]
    
    manager = InventoryManager()
    manager.agregar_algoritmo("FIFO", FIFOInventory())
    manager.agregar_algoritmo("LIFO", LIFOInventory())
    manager.agregar_algoritmo("JIT", JITInventory())
    
    manager.set_strategy("FIFO")
    print("Inventario optimizado con FIFO:", manager.optimize_inventory(stock))
    
    clone = manager.clone_version()
    clone.set_strategy("JIT")
    print("Inventario optimizado con JIT en clon:", clone.optimize_inventory(stock))