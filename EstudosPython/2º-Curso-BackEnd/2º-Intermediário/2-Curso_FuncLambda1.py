'''
Função Lambda
'''
# Ordem de preço crescente
produtos = [
    ['Produto 1', 10],
    ['Produto 2', 4],
    ['Produto 3', 5],
    ['Produto 4', 22],
    ['Produto 5', 21],
]
produtos.sort(key=lambda i: i[1])
print(produtos)
