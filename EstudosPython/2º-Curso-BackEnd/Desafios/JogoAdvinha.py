# Desafio de jogo de advinhação

palavra_secreta = 'python'  # Qualquer palavra
letra_digitada = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!!')
        continue

    letra_digitada.append(letra)

    if letra in palavra_secreta:
        print(f'A letra {letra} existe na palavra!')
    else:
        print(f'A letra {letra} não existe na palavra secreta!')
        letra_digitada.pop()

    secreto2 = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_digitada:
            secreto2 += letra_secreta
        else:
            secreto2 += '*'

    if secreto2 == palavra_secreta:
        print(f'Parabéns, você ganhou!! A palavra é {secreto2}.')
        break
    else:
        print(f'{secreto2}')

    if letra not in palavra_secreta:
        chances -= 1

    print(f'Chances restantes: {chances}')
