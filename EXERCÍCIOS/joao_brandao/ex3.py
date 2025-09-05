class ListaDeTarefas:
    def __init__(self):
        self._tarefas = [] 

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def remover(self, tarefa):
        self._tarefas.remove(tarefa)

    def __len__(self):
        """Permite usar len(lista)."""
        return len(self._tarefas)

    def __getitem__(self, indice):
        """Permite acessar tarefas[i] e iterar em for."""
        return self._tarefas[indice]

    def __str__(self):
        """Exibe todas as tarefas numeradas."""
        return "\n".join(f"{i+1}. {t}" for i, t in enumerate(self._tarefas))


lista = ListaDeTarefas()
lista.adicionar("Estudar Python")
lista.adicionar("Fazer exercícios")
lista.adicionar("Revisar anotações")

print(len(lista))        
print(lista[1])          

for tarefa in lista:    
    print("-", tarefa)

print("\nLista completa:")
print(lista)
