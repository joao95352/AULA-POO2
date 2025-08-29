class Relogio:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"


relogio = Relogio(0, 0)

while True:
    print("\n=== Painel do Relógio ===")
    print("1 - Ver hora")
    print("2 - Ajustar hora")
    print("3 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        print("Horário atual:", relogio)
    elif opc == "2":
        h = int(input("Digite a hora (0-23): "))
        m = int(input("Digite os minutos (0-59): "))
        relogio.hora, relogio.minuto = h, m
        print("Hora ajustada!")
    elif opc == "3":
        break
    else:
        print("Opção inválida")
