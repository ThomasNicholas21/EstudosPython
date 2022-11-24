""" 
 Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
 Escreva para cada X e Y uma
 mensagem que indique se estes valores foram
 digitados em ordem crescente ou decrescente.
 O programa deve finalizar quando forem digitados dois valores iguais.

"""
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

while x != y:
    if x > y:
        print(f'Ordem decrescente: {x} : {y}')
    else:
        print(f'Ordem crescente: {x} : {y}')
        print('')

    x = int(input('Digite o valor de x: '))
    y = int(input('Digite o valor de y: '))
