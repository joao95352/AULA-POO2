#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXERCÍCIO 4: Classe abstrata Forma com método area() e implementação Quadrado
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("Lado deve ser positivo")
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def __str__(self):
        return f"Quadrado com lado {self.lado}"


def testar_exercicio4():
    """Função para testar o exercício 4"""
    print("4. TESTE DA CLASSE ABSTRATA FORMA E QUADRADO:")
    print("-" * 30)
    quadrado = Quadrado(5)
    print(f"Forma: {quadrado}")
    print(f"Área: {quadrado.area()}")
    print(f"Perímetro: {quadrado.perimetro()}")
    
    try:
        quadrado_invalido = Quadrado(-3)
    except ValueError as e:
        print(f"Erro capturado: {e}")
    print()


if __name__ == "__main__":
    testar_exercicio4() 