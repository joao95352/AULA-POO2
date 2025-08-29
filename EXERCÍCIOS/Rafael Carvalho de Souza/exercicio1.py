class Livro:
    def __init__(self, titulo, estoque=0):
        self.titulo = titulo
        self._estoque = estoque

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor


livro = Livro("Livro", 10)

while True:
    print("\n=== MENU ===")
    print("1 - Ver estoque")
    print("2 - Alterar estoque")
    print("3 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        print(f"Estoque atual de '{livro.titulo}': {livro.estoque}")
    elif opc == "2":
        try:
            novo = int(input("Novo valor de estoque: "))
            livro.estoque = novo
            print("Estoque atualizado!")
        except ValueError as e:
            print("Erro:", e)
    elif opc == "3":
        break
    else:
        print("Opção inválida")
