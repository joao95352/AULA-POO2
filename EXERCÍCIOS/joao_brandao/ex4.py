from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        """Deve retornar a área da forma."""
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado



q = Quadrado(5)
print("Área do quadrado:", q.area())  

try:
    f = Forma()
except TypeError as e:
    print("Erro:", e)