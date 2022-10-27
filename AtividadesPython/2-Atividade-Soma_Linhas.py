# Fazer um programa para ler dois números inteiros M e N (máximo = 10).
# Em seguida, ler uma matriz
# Gerar um vetor de modo que cada elemento do vetor
# seja a soma dos elementos da linha correspondente da matriz.
# Mostrar o vetor gerado.

m = int(input('Numero de linhas: '))
n = int(input('Numero de colunas: '))
while m > 10 or n > 10:
    print('Valor deve ser no máximo 10!')
    m = int(input('Numero de linhas: '))
    n = int(input('Numero de colunas: '))

matriz = [[0 for x in range(n)]for x in range(m)]
vetor = [0 for x in range(m)]

for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input('Digite os elementos da linha: '))

for i in range(m):
    somalinha = 0
    for j in range(n):
        somalinha = somalinha + matriz[i][j]
    vetor[i] = somalinha

for i in range(m):
    print(f'{vetor[i]:.1f}')
