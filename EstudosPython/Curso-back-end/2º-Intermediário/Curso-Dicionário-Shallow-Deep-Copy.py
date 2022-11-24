"""
Shallow copy - copia rasa  copy()
deep copy - copia profunda deepcopy()
"""

import copy


d1 = {
    'Endereço 1': 'x',
    'Endereço 2': 'y',
    'Endereço 3': 'z',
}

d2 = copy.deepcopy(d1)

print(d1)
print(d2)
