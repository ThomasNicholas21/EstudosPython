import math

quadrado: float
raiz: float

num1 = float(input('Digite um valor: '))

if num1 > 0:
    quadrado = math.pow(num1, 2)
    raiz = math.sqrt(num1)
    print(f'O quadrado do numero é {quadrado:.2f} e a raiz é {raiz:.2f}')
else:
    print('Escolha um numero positivo!')
