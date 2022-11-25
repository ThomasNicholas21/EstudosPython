"""
qual o 1337º numero primo
"""

posicao = int(input('Digite a posicao: '))
posicao_contador = 0
n = 0
contador = 0
multiplo = 0

while True:
    n += 1
    contador += 1
    if n % contador == 0:
        multiplo += 1

    if multiplo == 0:
        print(n)
