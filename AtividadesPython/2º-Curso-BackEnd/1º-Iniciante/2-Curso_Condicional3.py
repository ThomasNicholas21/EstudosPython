import math

num1 = float(input('Digite o valor: '))
raiz = float
quadrado = float

if num1 > 0:
    raiz = math.sqrt(num1)
    print(f'O valor da raiz {raiz}')
else:
    quadrado = math.pow(num1, 2)
    print(f'O valor do numero ao quadrado: {quadrado}')
