#revisando modulos do Python
import sys       # importar inteiro não faz diferenca para python
                  
print(sys.platform)


from sys import platform # Nestes caso deve ter cuidado para não sobrescrever outra variável

print(platform)
      
from sys import platform as p # Mëtodo de contornar caso haja uma variável igual ao módulo, "má pratica".

print(p)

from sys import * # Má pratica de programacao

print(sys.exit)
print(sys.platform)

# https://docs.python.org/3/py-modindex.html fonte de estudo
