# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 1', 'preco': 12.50},
    {'nome': 'Produto 2', 'preco': 22.12},
    {'nome': 'Produto 5', 'preco': 10.66},
    {'nome': 'Produto 4', 'preco': 120.22},
    {'nome': 'Produto 3', 'preco': 88.36},
]

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda produto: produto['nome'], 
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda produto: produto['preco']
)

print('Produtos e precos: ')
print(*produtos, sep='\n')
print()
print('Novos precos: ')
print(*novos_produtos, sep='\n')
print()
print('Ordenando por nome: ')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('Ordenando por preco: ')
print(*produtos_ordenados_por_preco, sep='\n')
print()