from abc import ABC, abstractmethod

# --- Ejercicio 1: Algoritmos de Ordenación (Strategy) ---
class SortingStrategy(ABC):
  @abstractmethod
  def sort(self, lista, orden):
    pass

class BubbleSort(SortingStrategy):
  def sort(self, lista, orden):
    n = len(lista)
    for i in range(n):
      for j in range(0, n-i-1):
        if (orden == 'ascendente' and lista[j] > lista[j+1]) or (orden == 'descendente' and lista[j] < lista[j+1]):
          lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

class QuickSort(SortingStrategy):
  def sort(self, lista, orden):
    if len(lista) <= 1:
      return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot] if orden == 'ascendente' else [x for x in lista if x > pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot] if orden == 'ascendente' else [x for x in lista if x < pivot]
    return self.sort(left, orden) + middle + self.sort(right, orden)

class InsertionSort(SortingStrategy):
  def sort(self, lista, orden):
    for i in range(1, len(lista)):
      key = lista[i]
      j = i - 1
      if orden == 'ascendente':
        while j >= 0 and key < lista[j]:
          lista[j + 1] = lista[j]
          j -= 1
      elif orden == 'descendente':
        while j >= 0 and key > lista[j]:
          lista[j + 1] = lista[j]
          j -= 1
      lista[j + 1] = key
    return lista

class Sorter:
  def __init__(self, strategy: SortingStrategy):
    self.strategy = strategy

  def set_strategy(self, strategy: SortingStrategy):
    self.strategy = strategy

  def sort(self, lista, orden):
    return self.strategy.sort(lista, orden)
  
if __name__ == "__main__":
    sorter = Sorter(QuickSort())
    print("Ordenado:", sorter.sort([5, 3, 8, 2], "ascendente"))
    sorter.set_strategy(BubbleSort())
    print("Ordenado:", sorter.sort([5, 3, 8, 2], "descendente"))
    sorter.set_strategy(InsertionSort())
    print("Ordenado:", sorter.sort([5, 3, 8, 2], "ascendente"))