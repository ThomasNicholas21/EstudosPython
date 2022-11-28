"""
Advinha com SET
"""

palavra_secreta = 'python'
letras_digitadas = set()
chances = 3

while True:
    if chances <= 0:
        print('Perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite uma letra!')
        continue

    if letra.isdigit():
        print('Digite uma letra!')
        continue

    letras_digitadas.add(letra)

    if letra in palavra_secreta:
        print(f'A letra {letra} existe na palavra!')
    else:
        print(f'A letra {letra} não existe na palavra secreta!')
        letras_digitadas.discard(letra)

    palavra_secreta2 = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_secreta2 += letra_secreta
        else:
            palavra_secreta2 += '*'

    if palavra_secreta2 == palavra_secreta:
        print(f'Você ganhou! A palavra secreta é {palavra_secreta2}')
        break
    else:
        print(f'{palavra_secreta2}')

    if letra not in palavra_secreta:
        chances -= 1
    print(f'Seu número de chance é {chances}')
