"""
qual o 1337º numero primo
"""


def primo(n):
    multiplo = 0
    for numero in range(2, n):
        if n % numero == 0:
            multiplo += 1
    if multiplo == 0:
        return True
    return False


posicao = int(input('Digite qual posição do número primo: '))
numeros = 0
numero = 1

while numeros != posicao:
    numero += 1
    if primo(numero) is True:
        numeros += 1
        if numeros == posicao:
            print(numero)
    else:
        continue
