class LogFile:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, "a", encoding="utf-8")
        self.arquivo.write("=== Começo da sessão ===\n")
        return self.arquivo

    def __exit__(self, tipo, valor, traceback):
        self.arquivo.write("=== Fim da sessão ===\n\n")
        self.arquivo.close()


nome = "log.txt"

while True:
    print("\n=== MENU ===")
    print("1 - Escrever no log")
    print("2 - Ler log completo")
    print("3 - Limpar log")
    print("4 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        msg = input("Digite a mensagem: ")
        with LogFile(nome) as log:
            log.write(msg + "\n")
        print("Mensagem registrada!")
    elif opc == "2":
        try:
            with open(nome, "r", encoding="utf-8") as f:
                print("\n--- Conteúdo do log ---")
                print(f.read())
        except FileNotFoundError:
            print("Log ainda não existe.")
    elif opc == "3":
        open(nome, "w").close()
        print("Log limpo!")
    elif opc == "4":
        break
    else:
        print("Opção inválida")
