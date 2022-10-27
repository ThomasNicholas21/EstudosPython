# Leia 2 valores inteiros X e Y (em qualquer ordem).
# A seguir, calcule e mostre a soma dos números
# impares entre eles.
z: int
soma: int
soma = 0

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))

if x > y:
    z = x
    x = y
    y = z

for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + 1

print(f'Soma dos numeros impares: {soma}')
