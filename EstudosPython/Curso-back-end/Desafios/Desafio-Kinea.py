"""
qual o 1337º numero primo
"""


def primo(n):
    multiplo = 0
    for numero in range(2,n):
        if n % numero == 0:
            multiplo += 1
    if multiplo == 0:
        return True
    return False

i = int(input('Digite qual posição do número primo: '))        
lista = 0
numero = 1

while lista != i:
    numero += 1
    if primo(numero) is True:
        lista += 1
        if lista == i:
            print(numero)
        #lista.append(numero)
    else:
        continue

#print(lista)



#print(lista[i-1])