"""
filtro em list comprehension
"""

# ordenamento de chaves 'sort_dicts=False'
# Largura de linha 'width=40'

import pprint


def output(valor):
    pprint.pprint(valor, sort_dicts=False, width=150)


produtos = [
    {'nome': 'mouse', 'preço': 55},
    {'nome': 'teclado', 'preço': 89},
    {'nome': 'monitor', 'preço': 256},
    {'nome': 'cadeira', 'preço': 398},
]

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    for produto in produtos
    if produto['preço'] > 100  # filtro
]
# ordenamento de chaves 'sort_dicts=False'
# Largura de linha 'width=40'

output(novos_produtos)
