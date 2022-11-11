"""
contador de letras
"""
frase = input('Digite uma frase ou uma palavra qualquer: ')

i = 0
contador_maisvezes = 0
letra_maisvezes = ''

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue

    contador_maisvezes_atual = frase.count(letra)

    if contador_maisvezes < contador_maisvezes_atual:
        contador_maisvezes = contador_maisvezes_atual
        letra_maisvezes = letra

    i += 1

print(
    'A letra que apareceu mais vezes : '
    f'"{letra_maisvezes}" e apareceu '
    f'{contador_maisvezes} vezes.'
)
