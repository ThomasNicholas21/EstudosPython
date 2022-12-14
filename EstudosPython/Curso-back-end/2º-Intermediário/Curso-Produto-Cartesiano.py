"""
produto cartesiano
"""
# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

conjuntoA = [1, 3, 4]
conjuntoB = [2, 3]
conjuntoAB = [
    [1, 3, 4],
    [2, 3]
]
for i in conjuntoA:
    for j in conjuntoB: 
        print(f'({i}, {j})')

print()
for i in conjuntoA:
    for j in conjuntoA:
        print(f'({i}, {j})')

print()
for i in conjuntoB:
    for j in conjuntoB:
        print(f'({i}, {j})')

print()
print_iter(combinations(conjuntoA, 2))  
print_iter(combinations(conjuntoB, 2))  
print_iter(permutations(conjuntoA, 2))  
print_iter(permutations(conjuntoB, 2))    
print_iter(product(*conjuntoAB))