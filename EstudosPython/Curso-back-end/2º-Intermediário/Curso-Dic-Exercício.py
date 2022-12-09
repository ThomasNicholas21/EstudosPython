from dic_pack import perguntas
from os import system

i = ['a', 'b', 'c', 'd']
qtd_acerto = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in opcoes.items():
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção ')

    acertou = False

    if escolha == pergunta['Resposta']:
        acertou = True
    
    if acertou:
        print('Acertoou 🥳')
    else:
        print('Errou 😥')
