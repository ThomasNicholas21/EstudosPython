# Dada uma lista, crie uma nova lista sem duplicatas.

lista_com_duplicatas = [1, 2, 3, 2, 4, 5, 6, 4]

lista_sem_duplicatas = [
    i for j, i in enumerate(lista_com_duplicatas)
    if i not in lista_com_duplicatas[:j]
]


print(lista_sem_duplicatas)
