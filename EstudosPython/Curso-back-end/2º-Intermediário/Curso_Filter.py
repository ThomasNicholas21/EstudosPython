produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]


novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)


print(*list(produtos), sep='\n')
print()
print(*list(novos_produtos), sep='\n')