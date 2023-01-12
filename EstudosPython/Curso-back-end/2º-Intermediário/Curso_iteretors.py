# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porc(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_porcentagem = partial(aumentar_porc, porcentagem=1.1)

# novos_produtos = [
#     {**p,
#     'preco': aumentar_porcentagem(p['preco'])}
#     for p in produtos
# ]

def muda_preco_produto(produto):
    return  {**produto,
    'preco': aumentar_porcentagem(produto['preco'])}
    

novos_produtos = map(
    muda_preco_produto, produtos
)


print_iter(produtos)
print_iter(novos_produtos)

print(list(
    map(
        lambda x: x * 3,
        [1, 2, 3, 4, 5, 6]
        )
    )
)
