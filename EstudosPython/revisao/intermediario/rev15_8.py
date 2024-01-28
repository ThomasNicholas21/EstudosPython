# Dadas duas listas, crie uma lista que contenha todas as combinações de elementos das duas listas.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = [
    (i, j) for i in lista1 for j in lista2
]


print(*lista3, sep='-')