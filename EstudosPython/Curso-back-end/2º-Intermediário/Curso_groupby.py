from itertools import groupby


grupos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Jefferson', 'nota': 'C'},
    {'nome': 'Thomas', 'nota': 'D'},
    {'nome': 'Nicholas', 'nota': 'A'},
    {'nome': 'Roberto', 'nota': 'A'},
    {'nome': 'Carol', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'F'},
]
def ordena(grupo):
    return grupo['nota']

alunos_grupos = sorted(grupos, key=ordena)
alunos = groupby(alunos_grupos, key=ordena)

for chave, grupo in alunos:
    print(chave)
    for aluno in grupo:
        print(aluno)
