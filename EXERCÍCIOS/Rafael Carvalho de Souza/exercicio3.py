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

while True:
    print("\n=== Painel de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver todas as tarefas")
    print("3 - Ver tarefa específica")
    print("4 - Total de tarefas")
    print("5 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        t = input("Digite a tarefa: ")
        lista.adicionar(t)
        print("Tarefa adicionada!")
    elif opc == "2":
        print("Tarefas:")
        for t in lista:
            print("-", t)
    elif opc == "3":
        idx = int(input("Número da tarefa (0 até n-1): "))
        try:
            print("Tarefa:", lista[idx])
        except IndexError:
            print("Índice inválido")
    elif opc == "4":
        print("Total de tarefas:", len(lista))
    elif opc == "5":
        break
    else:
        print("Opção inválida")
