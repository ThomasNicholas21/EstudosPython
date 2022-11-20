
while True:
    qtd = input('Digite a quantidade de linhas: ')
    qtd2 = input('Digite a quantidade de colunas: ')

    if not qtd.isnumeric() or not qtd2.isnumeric():
        print('Digite numeros!')
        continue

    qtd = int(qtd)
    qtd2 = int(qtd2)

    linha = 1
    while linha <= qtd:
        coluna = 1
        while coluna <= qtd2:
            coluna += 1
            multiplicação = linha*coluna
            print(f'{linha=} : {coluna=} : {multiplicação=}')
        linha += 1

    print('Multiplicação de linha e coluna finalizada!')

    sair = input('Deseja sair? [S]im ou [N]ão : ').lower().startswith('s')
    if sair is True:
        print('Obrigado!')
        break
