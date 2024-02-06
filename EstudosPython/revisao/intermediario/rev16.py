# Aprendendo a mapear e filtrar dados

produtos = [
    {'nome': 'p1', 'preco': 20.1, },
    {'nome': 'p2', 'preco': 10.5, },
    {'nome': 'p3', 'preco': 30.2, },
    {'nome': 'p4', 'preco': 42,   },
    {'nome': 'p5', 'preco': 50.5, },
]

novos_produtos = [
    {**produto, 'preco' : round(produto['preco'] * 1.75, 2)} # realizando o mapeamento de dados com condicoes estabelecidas
    if produto['preco'] < 25 else {**produto} # tudo que esta a direita da repeticao, sera mapeamento de dado
    for produto in produtos
    if produto['preco'] > 19 # filtrando por produtos maiores que 19, tudo a direita do for sera filtro
]

print(*produtos, sep= '\n') # visualizando a primeira lista de produtos
print()
print(*novos_produtos, sep= '\n') # visualizando a segunda lista de produtos