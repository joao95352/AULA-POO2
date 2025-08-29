from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


while True:
    print("\n=== Painel de Formas ===")
    print("1 - Calcular área do quadrado")
    print("2 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        lado = float(input("Digite o lado do quadrado: "))
        q = Quadrado(lado)
        print("Área:", q.area())
    elif opc == "2":
        break
    else:
        print("Opção inválida")
