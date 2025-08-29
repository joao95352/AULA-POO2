class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def __len__(self):
        return len(self.tarefas)

    def __getitem__(self, index):
        return self.tarefas[index]

    def __iter__(self):
        return iter(self.tarefas)


lista = ListaDeTarefas()
lista.adicionar("Estudar Python")
lista.adicionar("Fazer exercícios")
print(len(lista))       
for t in lista:
    print(t)
print(lista[0])         