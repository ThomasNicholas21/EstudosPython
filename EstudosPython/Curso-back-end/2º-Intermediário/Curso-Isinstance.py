"""
Utilizando isinstance
"""

lista = [
    'a', 22, True, [0, 1, 2, 3, 4], (1, 2),
    {22, 22, 12}, {'jogador': 'Neymar'},
]

for item in lista:
    if isinstance(item, set):
        item.add(985)
        print(item, isinstance(item, set))

    elif isinstance(item, dict):
        print(item, isinstance(item, dict))

    elif isinstance(item, (int, float)):
        print(item, item * 2)

    else:
        print('-')
