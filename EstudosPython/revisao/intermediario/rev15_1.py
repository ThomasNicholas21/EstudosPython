#Crie uma lista com os quadrados dos números de 1 a 10.

lista = [
    numero * 2
    for numero in range(1,11)
]

print(*lista, sep='-')