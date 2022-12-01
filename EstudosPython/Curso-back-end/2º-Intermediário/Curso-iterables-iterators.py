"""
iterables e iterators
"""
# iterators fornece uma maneira de acessar
# sequencialmente os elementos de um objeto
# agregado sem expor sua representação subjacente

iterable = ['Thomas', 'Nicholas', '__iter__']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
