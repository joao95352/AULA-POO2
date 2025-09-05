class Relogio:
    def __init__(self, hora: int, minuto: int):
        self.hora = hora % 24
        self.minuto = minuto % 60

    def __str__(self):
        return f"🕒 {self.hora:02d}:{self.minuto:02d}"


if __name__ == "__main__":
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))

    relogio = Relogio(hora, minuto)
    print("Horário formatado:", relogio)
