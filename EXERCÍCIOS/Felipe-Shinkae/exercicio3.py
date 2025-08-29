#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXERCÍCIO 3: Classe ListaDeTarefas que funcione com len(), for e tarefas[i]
"""

class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self._tarefas.append(tarefa)
    
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self._tarefas):
            return self._tarefas.pop(indice)
        raise IndexError("Índice fora do intervalo")
    
    def __len__(self):
        return len(self._tarefas)
    
    def __getitem__(self, indice):
        return self._tarefas[indice]
    
    def __iter__(self):
        return iter(self._tarefas)
    
    def __str__(self):
        if not self._tarefas:
            return "Lista de tarefas vazia"
        return "\n".join([f"{i+1}. {tarefa}" for i, tarefa in enumerate(self._tarefas)])


def testar_exercicio3():
    """Função para testar o exercício 3"""
    print("3. TESTE DA CLASSE LISTA DE TAREFAS:")
    print("-" * 30)
    tarefas = ListaDeTarefas()
    tarefas.adicionar_tarefa("Estudar Python")
    tarefas.adicionar_tarefa("Fazer exercícios")
    tarefas.adicionar_tarefa("Revisar código")
    
    print(f"Lista de tarefas: {tarefas}")
    print(f"Número de tarefas: {len(tarefas)}")
    print(f"Primeira tarefa: {tarefas[0]}")
    print("Iterando pelas tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"  {i+1}. {tarefa}")
    print()


if __name__ == "__main__":
    testar_exercicio3() 