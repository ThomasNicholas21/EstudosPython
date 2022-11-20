"""
 Fazer um programa para ler um número inteiro N (máximo = 10) e
 uma matriz quadrada de ordem N
 contendo números inteiros.
 Em seguida, mostrar a diagonal principal e a
 de valores negativos da matriz.

"""

N = int(input('Qual será a ordem da matriz? ፡ '))
while N > 10:
    print('Insira um valor menor que 10!')
    N = int(input('Qual será a ordem da matriz? ፡ '))

matriz = [[0 for l in range(N)]for l in range(N)]

for i in range(0, N):
    for j in range(0, N):
        matriz[i][j] = int(input(f'[{i},{j}]: '))

for i in range(0, N):
    print(f'{matriz[i][i]}')

cont = 0
for i in range(0, N):
    for j in range(0, N):
        if matriz[i][j] < 0:
            cont = + 1

print(f'Quantidade de valores negativos: {cont}')
