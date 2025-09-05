class Relogio:
    def __init__(self, hora=0, minuto=0):
        if not (0 <= hora < 24):
            raise ValueError("Hora deve estar entre 0 e 23.")
        if not (0 <= minuto < 60):
            raise ValueError("Minuto deve estar entre 0 e 59.")
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"


r1 = Relogio(9, 5)
print(r1) 

r2 = Relogio(23, 45)
print(r2) 