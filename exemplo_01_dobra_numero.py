import random
import time

def ler_ultimo_numero():
    try:
        with open('numeros.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                return int(lines[-1].strip())
            else:
                print('Arquivo está vazio')
                return None
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return None

def dobra_numero(num):
    return num * 2

if __name__ == "__main__":
    while True:
        num = ler_ultimo_numero()
        if num is not None:
            resultado = dobra_numero(num)
            print(f'O dobro de {num} é {resultado}')
            time.sleep(1)
