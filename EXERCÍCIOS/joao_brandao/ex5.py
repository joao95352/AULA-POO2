class AbreFecha:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, "a", encoding="utf-8")
        self.arquivo.write("Começo\n")
        return self.arquivo 

    def __exit__(self, tipo, valor, traceback):
        self.arquivo.write("Fim\n")
        self.arquivo.close()
        return False


with AbreFecha("log.txt") as f:
    f.write("Dentro do bloco\n")

print("Arquivo log.txt atualizado!")
