#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXERCÍCIO 1: Classe Livro com @property para estoque que proíba números negativos
"""

class Livro:
    def __init__(self, titulo, autor, estoque=0):
        self._titulo = titulo
        self._autor = autor
        self._estoque = estoque
    
    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo!")
        self._estoque = valor
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    def __str__(self):
        return f"'{self._titulo}' por {self._autor} - Estoque: {self._estoque}"


def testar_exercicio1():
    """Função para testar o exercício 1"""
    print("1. TESTE DA CLASSE LIVRO:")
    print("-" * 30)
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 10)
    print(f"Livro criado: {livro}")
    
    try:
        livro.estoque = -5
    except ValueError as e:
        print(f"Erro capturado: {e}")
    
    livro.estoque = 15
    print(f"Estoque atualizado: {livro}")
    print()


if __name__ == "__main__":
    testar_exercicio1() 