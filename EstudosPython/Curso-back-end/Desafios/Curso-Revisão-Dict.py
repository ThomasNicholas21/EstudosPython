"""
Será um esquema de perguntas e respostas para
revisão de dict
"""

quantidade_de_acertos = 0
perguntas = [
{
    'Pergunta': 'Qual dos seguintes tipos de dados são mutáveis?',
    'Opções': ['Int', 'Float', 'List', 'Tuple'],
    'Resposta': 'List',
},
{
    'Pergunta': 'Quais dos seguintes comando insere valor no final da lista?',
    'Opções': ['Pop', 'Clear', 'Join', 'Append'],
    'Resposta': 'Append',
},
{
    'Pergunta': 'O comando Sort é usado pra que?',
    'Opções': ['deletar', 'dividir', 'Limpar', 'Ordenar'],
    'Resposta': 'Ordenar',
},
{
    'Pergunta': 'Qual a biblioteca que permite obter o horário atual?',
    'Opções' : ['datefns', 'moment', 'stdlib.h', 'datetime'],
    'Resposta': 'datetime',
},
]

quantidade_de_acertos = 0
for pergunta in perguntas:
    print('Perguntas:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Digite sua resposta: ')

    acerto = True
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acerto = True
    
    print()
    if acerto:
        quantidade_de_acertos += 1
        print('Acertou 😎')
    else:
        print('Errou 😢')

print(f'Você acertou {quantidade_de_acertos} de {len(perguntas)}')