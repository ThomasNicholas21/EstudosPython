"""
Utilizando Kwargs como visto na aula
"""


def argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor, sep='-')
    print()


pessoa_dados_principais = {
    'Nome': 'Thomas',
    'Idade': '22',
    'email': 'thomasnicholaas@gmail.com',
    'ocupação': 'estudante',
    'Aonde mora': 'Anápolis',
}

pessoa_dados_secundarios = {
    'Hobbie': 'Tocar violão',
    'Frequenta academia': 'Sim',
    'Assisti séries': 'Sim',
    'Comida favorita': 'Hamburguer',
}

argumentos_nomeados(**pessoa_dados_principais)
argumentos_nomeados(**pessoa_dados_secundarios)
