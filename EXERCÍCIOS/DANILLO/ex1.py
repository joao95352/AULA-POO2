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
            raise ValueError("O estoque não pode ser negativo.")
        self._estoque = valor


livro = Livro("Python Básico", 10)
print(livro.estoque)  
livro.estoque = 5
print(livro.estoque) 
