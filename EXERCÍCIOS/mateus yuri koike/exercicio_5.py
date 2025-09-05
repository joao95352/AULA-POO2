class Registro:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self._f = None

    def __enter__(self):
        self._f = open(self.arquivo, "a", encoding="utf-8")
        self._f.write("🔹 Começo\n")
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.write("🔸 Fim\n")
        self._f.close()


if __name__ == "__main__":
    with Registro("log.txt") as log:
        msg = input("Digite uma mensagem para registrar no log: ")
        log.write(msg + "\n")

    print("✅ Mensagem registrada em log.txt")
