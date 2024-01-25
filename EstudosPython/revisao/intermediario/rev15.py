#list comprehension - revisando

lista = [1,2,3,4,5]

nova_lista = [
    iterador * 2 
    for iterador in lista
]

print(*nova_lista, sep='-')