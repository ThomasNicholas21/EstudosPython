"""
produto cartesiano
"""

conjuntoA = [1, 3, 4]
conjuntoB = [2, 3]

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