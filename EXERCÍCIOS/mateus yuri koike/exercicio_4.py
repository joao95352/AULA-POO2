from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def __str__(self):
        return f"⬛ Quadrado com lado {self.lado} | Área = {self.area()}"


if __name__ == "__main__":
    lado = float(input("Digite o lado do quadrado: "))
    q = Quadrado(lado)
    print(q)
