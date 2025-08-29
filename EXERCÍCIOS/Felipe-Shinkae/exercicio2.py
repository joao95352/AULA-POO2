#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXERCÍCIO 2: Classe Relogio que sobrecarrega __str__ para mostrar HH:MM
"""

class Relogio:
    def __init__(self, hora=0, minuto=0):
        self.hora = hora
        self.minuto = minuto
    
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"
    
    def set_hora(self, hora, minuto):
        if 0 <= hora <= 23 and 0 <= minuto <= 59:
            self.hora = hora
            self.minuto = minuto
        else:
            raise ValueError("Hora inválida! Use 0-23 para hora e 0-59 para minuto")


def testar_exercicio2():
    """Função para testar o exercício 2"""
    print("2. TESTE DA CLASSE RELÓGIO:")
    print("-" * 30)
    relogio = Relogio(14, 30)
    print(f"Relógio: {relogio}")
    
    relogio.set_hora(9, 15)
    print(f"Relógio atualizado: {relogio}")
    
    try:
        relogio.set_hora(25, 70)
    except ValueError as e:
        print(f"Erro capturado: {e}")
    print()


if __name__ == "__main__":
    testar_exercicio2() 