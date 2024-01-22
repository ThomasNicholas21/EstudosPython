#Aplicando revisão, jogo de pergunta e resposta com dicionário

perguntas = [
    {
        'Pergunta' : 'Quanto é 24 x 3?',
        'Opções' : ['72', '62', '82', '78'],
        'Resposta' : '72',
    },
    {
        'Pergunta' : 'Qual a capital do Canada?',
        'Opções' : ['Vancouver', 'Ottawa', 'Quebec', 'Montreal'],
        'Resposta' : 'Ottawa',
    },
    {
        'Pergunta' : 'Qual animal é um mamifero?',
        'Opções' : ['Pato', 'Ornitorrinco', 'Pinguim', 'Aranha'],
        'Resposta' : 'Ornitorrinco',
    },
]

acerto = 0
erro = 0

for chave in perguntas:
    print('Pegunta:', chave['Pergunta'])

    opcoes = chave['Opções']
    for i, j in enumerate(opcoes):
        print(f'{i})', j)

    resposta = input('Digite sua resposta: ')
    resposta_int = None
    quantidade_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < quantidade_opcoes:
            if opcoes[resposta_int] == chave['Resposta']:
                print('Correta a resposta!!\n')
                acerto += 1   
            else:
                print('Resposta incorreta!!\n')
                erro += 1
                
if acerto == 3:
    print(f'Parabéns, você acertou {acerto} perguntas!! 😊')
elif acerto == 2:
    print(f'Quase la!! Você acertou {acerto} perguntas!! 👌')
elif acerto == 1:
    print(f'Nossa!! Essa foi por pouco, você acertou {acerto} pergunta!! 🙌')
else:
    print(f'Você errou {erro} perguntas 😢')