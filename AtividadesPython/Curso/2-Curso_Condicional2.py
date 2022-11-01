import math

num1 = float(input('Digite um valor: '))
raiz: float

if num1 > 0:
    raiz = math.sqrt(num1)
    print(f'O valor da raiz de {num1} é {raiz}')
else:
    print('Numero invalido!')
