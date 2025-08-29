class Log:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def __enter__(self):
        self.file = open(self.arquivo, "a", encoding="utf-8")
        self.file.write("Começo\n")
        return self.file

    def __exit__(self, tipo, valor, traceback):
        self.file.write("Fim\n")
        self.file.close()


with Log("log.txt") as f:
    f.write("Executando algo...\n")