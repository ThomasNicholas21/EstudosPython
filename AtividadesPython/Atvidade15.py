from cmath import pi
import math

radianos = float(input('Digite o valor do angulo em radianos: '))

graus = (radianos*180)/pi

print(f'O valor do angulo em graus: {graus:.2f}')
