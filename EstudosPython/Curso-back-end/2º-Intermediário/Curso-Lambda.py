"""
Utilizando a função lambda 
"""

lista = [
    {'nome': 'Thomas', 'sobrenome': 'Matias'},
    {'nome': 'Douglas', 'sobrenome': 'Silva'},
    {'nome': 'Rodrigo', 'sobrenome': 'Fernandes'},
    {'nome': 'Adalberto', 'sobrenome': 'Ferreira'},
    {'nome': 'João', 'sobrenome': 'Augustus'},
    {'nome': 'Fernando', 'sobrenome': 'Rodrigo'},
]


def tabela(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['nome'], reverse=True)

tabela(l1)
tabela(l2)
