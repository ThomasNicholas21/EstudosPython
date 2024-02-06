#Dadas duas listas, crie uma terceira lista que contenha o produto dos elementos correspondentes das duas listas.

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,1]

valor_correspondente = [
    a * b
    for a, b in zip(lista1, lista2) #Itera sobre iteraveis, retorando eles em tuplas
]

print(*valor_correspondente)

#Como funciona por baixo dos panos - zip
# def zip_custom(*iterables):
#     Cria um iterador para cada entrada
#     iterators = [iter(iterable) for iterable in iterables]

#     Continua até que o menor iterador esteja esgotado
#     while True:
#         try:
#             Obtém o próximo elemento de cada iterador
#             yield tuple(next(iterator) for iterator in iterators)
#         except StopIteration:
#             Se um iterador está esgotado, termina o loop
#             return
