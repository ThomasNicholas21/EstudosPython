# Revisando generator, iterators e iterables
# Generetor expression são funções que conseguem pausar - todo generator é um iterator
# iterator é uma classe que depende de um iterable para "navegar" dentro dele - iterator não é generator
import sys

generator = (n*2 for n in range(100)) # ele só entrega um valor por vez, assim ocupa menos espaço
print(generator)
print(sys.getsizeof(generator))

# diferentemente da lista, generator não consegue acessar elementos, ele so sabe o proximo
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))