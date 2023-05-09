from functools import partial

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_valor = partial(aumentar_porcentagem, porcentagem=5.5)

# novos_produtos = [
#     {**p, 'preco': aumentar_valor(p['preco'])}
#     for p in produtos
# ]

def aumentar(produto):
      return {
        **produto,
        'preco': aumentar_valor(
            produto['preco']
        )
    }

novos_produtos = map(aumentar, produtos)

print(*list(produtos), sep='\n')
print()
print(*list(novos_produtos), sep='\n')