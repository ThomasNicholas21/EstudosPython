#Dadas duas listas, crie uma terceira lista que contenha o produto dos elementos correspondentes das duas listas.

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,1]

valor_correspondente = [
    a * b
    for a, b in zip(lista1, lista2)
]

print(*valor_correspondente)