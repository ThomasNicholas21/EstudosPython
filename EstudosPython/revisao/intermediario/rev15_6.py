# Dada uma lista de palavras, crie uma nova lista contendo cada palavra invertida.


lista_palavras = ['Thomas', 'Samara', 'Ana', 'Python', 'Anel', 'Dedo', 'mão']

lista_palavras_invertidas = [
    x[::-1]
    for x in lista_palavras
]

print(*lista_palavras_invertidas)
