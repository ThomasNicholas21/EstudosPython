"""
trabalhando com set
"""

# set1 = set()
# set1.add('Thomas')
# set1.add(1)
# set1.update(('Hello World', 1, 2, 3, 4))
# set1.discard('Hello World')
# print(set1)

A = {1, 2, 3}
B = {4, 2, 5}
c = A | B  # Une dois sets
d = A & B  # Itens que estáo em ambos
e = A - B  # Mostra a diff entre os sets
f = A ^ B  # itens que n estao em ambos
print(c)
print(d)
print(f)
