class Livro:
    def __init__(self, titulo, autor, estoque=0):
        self.titulo = titulo
        self.autor = autor
        self._estoque = 0
        self.estoque = estoque

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("❌ Estoque não pode ser negativo.")
        self._estoque = valor

    def __str__(self):
        return f"📚 '{self.titulo}' - {self.autor} | Estoque: {self.estoque}"


def ler_inteiro(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v < 0:
                print("❌ Estoque não pode ser negativo. Tente novamente.")
                continue
            return v
        except ValueError:
            print("❌ Digite um número inteiro válido.")


if __name__ == "__main__":
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")
    estoque_inicial = ler_inteiro("Digite o estoque inicial: ")

    livro = Livro(titulo, autor, estoque_inicial)
    print(livro)

    while True:
        entrada = input("Atualize o estoque (Enter para sair): ").strip()
        if entrada == "":
            break
        try:
            livro.estoque = int(entrada)
            print("📖 Atualizado:", livro)
        except ValueError:
            print("❌ Valor inválido ou negativo.")
