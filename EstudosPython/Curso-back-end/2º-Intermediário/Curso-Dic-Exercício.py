from dic_pack import perguntas, abcd

i = ['a', 'b', 'c', 'd']
qtd_acerto = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for opcao in opcoes:
        
    print()

    escolha = input('Escolha uma opção ')

    acertou = False
    escolha = None
    qtd_opcoes = len(opcoes)