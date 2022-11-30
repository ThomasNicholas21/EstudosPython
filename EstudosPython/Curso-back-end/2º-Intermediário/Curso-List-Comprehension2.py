"""
mapeamento list comprehension
"""

produtos = [
    {'nome': 'mouse', 'preço': 55},
    {'nome': 'teclado', 'preço': 89},
    {'nome': 'monitor', 'preço': 256},
    {'nome': 'cadeira', 'preço': 398},
]

# Regulagem dos preços
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.08}
    if produto['preço'] > 100 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')
