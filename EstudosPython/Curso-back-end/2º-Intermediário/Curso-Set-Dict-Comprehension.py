"""
Estudando set e dict comprehension
"""

dicionario = {
    'nome': 'Thomas',
    'idade': 22,
    'profissão': 'Engenheiro de software'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in dicionario.items()
}
print(dc)

set1 = {i**8 for i in range(10)}
print(set1)
