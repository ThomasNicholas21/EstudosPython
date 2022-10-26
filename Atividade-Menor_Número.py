# Fazer um programa para ler três números inteiros.
# Em seguida, mostrar qual o menor dentre os três
# números lidos. Em caso de empate, mostrar apenas uma vez.

a = int(input('Insira o primeiro valor:'))
b = int(input('Insira o segundo valor:'))
c = int(input('Insira o terceiro valor:'))

if a < b and a < c:
    print(F'Primero valor, é o menor: {a}.')
elif b < a and b < c:
    print(F'Segundo valor, é o menor: {b}.')
elif c < a and c < b:
    print(f'Terceiro valor, é o menor: {c}.')
elif a == b or a == c:
    print(f'O menor valor: {a}.')
else:
    print(f'O menor valor: {b}.')
