"""
generator expression, iterables e iterators
"""
# iterators fornece uma maneira de acessar
# sequencialmente os elementos de um objeto
# agregado sem expor sua representação subjacente
import sys

iterable = ['Thomas', 'Nicholas', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000)]
gerador = (n for n in range(1000))  # Generator expression
# generator é uma função que sabe pausar
# necessita do next para funcionar

# getsizeof pega o tamanho
print(sys.getsizeof(lista))
print(sys.getsizeof(gerador))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for n in gerador:
#     print(n)
