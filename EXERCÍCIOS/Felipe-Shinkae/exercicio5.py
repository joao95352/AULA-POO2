#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXERCÍCIO 5: "abre/fecha" simples com with que registre "Começo" e "Fim" num arquivo
"""

import time


class RegistradorArquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.arquivo = None
    
    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, 'a', encoding='utf-8')
        self.arquivo.write(f"Começo: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.arquivo:
            self.arquivo.write(f"Fim: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            self.arquivo.close()


def testar_exercicio5():
    """Função para testar o exercício 5"""
    print("5. TESTE DO CONTEXT MANAGER:")
    print("-" * 30)
    print("Executando operação com context manager...")
    
    with RegistradorArquivo("registro.txt") as reg:
        print("  Dentro do context manager - fazendo alguma operação...")
        time.sleep(1)  # Simula alguma operação
    
    print("Context manager finalizado. Verifique o arquivo 'registro.txt'")
    print()


if __name__ == "__main__":
    testar_exercicio5() 