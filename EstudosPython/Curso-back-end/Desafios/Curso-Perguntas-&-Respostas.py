"""
Programa com perguntas e respostas
"""
perguntas = [
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['Fortaleza', 'Brasilia', 'Recife', 'Goiânia'],
        'Resposta': 'Brasilia',
    },
    {
        'Pergunta': 'Quem vai ganhar a copa do mundo 2022?',
        'Opções': ['Brasil', 'Portugal', 'França', 'Espanha'],
        'Resposta': 'Brasil',

    },
    {
        'Pergunta': 'Quanto é 1x2x3x4x5?',
        'Opções': ['230', '140', '125', '120'],
        'Resposta': '120',
    },
    {
        'Pergunta': 'Quem tem a cabeça mais grande?',
        'Opções': ['Jonathan', 'Andrade', 'Nelli', 'Thomas'],
        'Resposta': 'Andrade',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    if escolha.isdigit():
        escolha_int = int(escolha)

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if escolha_int == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou!👍')
    else:
        print('Errou!❌')

    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas!')
