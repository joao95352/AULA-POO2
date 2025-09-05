class Livro:
    def __init__(self, titulo, autor, estoque):
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
            raise ValueError("O estoque não pode ser negativo.")
        self._estoque = valor

try:
    livro1 = Livro("1984", "George Orwell", 5)
    print(livro1.estoque)
    livro1.estoque = 10
    print(livro1.estoque)
    livro1.estoque = -3
except ValueError as e:
    print(e)
