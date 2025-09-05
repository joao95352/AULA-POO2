class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa: str):
        self._tarefas.append(tarefa)

    def __len__(self):
        return len(self._tarefas)

    def __getitem__(self, index):
        return self._tarefas[index]

    def __iter__(self):
        return iter(self._tarefas)


if __name__ == "__main__":
    lista = ListaDeTarefas()

    while True:
        tarefa = input("Adicione uma tarefa (ou 'sair' para terminar): ")
        if tarefa.lower() == "sair":
            break
        lista.adicionar(tarefa)

    print("\n📋 Suas tarefas:")
    for i, t in enumerate(lista, start=1):
        print(f"{i}. {t}")

    print(f"Total de tarefas: {len(lista)}")
