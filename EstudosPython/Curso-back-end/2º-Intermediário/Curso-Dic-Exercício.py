from dic_pack import perguntas
from os import system

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
        qtd_acerto += 1
        print('Acertoou 🥳\n')
    else:
        print('Errou 😥\n')

print(f'Parabéns, você acertou {qtd_acerto} de 4 perguntas')