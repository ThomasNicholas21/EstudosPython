"""
Aprendendo a utilizar dicionário
"""

# Primeiro modo
pessoa = {
    'nome': 'Thomas Nicholas',
    'idade': 22,
    'email': 'thomasnicholaas@gmail.com',
    'altura': 1.77,
    'endereços': [
        {'rua': 'x', 'número': 123},
        {'rua': 'y', 'número': 321},
    ],
}


for chave in pessoa:
    print(chave, '=', pessoa[chave])

# print(pessoa)
# print(pessoa['nome'])


# Segundo modo - menos usado
# pessoa = dict(nome='Thomas', idade='22 anos',
# email='thomasnicholaas@gmail.com')
