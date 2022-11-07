"""
calculo do IMC
"""
while True:
    nome = input('Digite seu nome: ')
    if nome.isnumeric():
        print('Digite seu nome sem numeros!')
        continue

    altura = input('Digite sua altura: ')
    peso = input('Digite seu peso: ')

    if altura.isnumeric() or peso.isnumeric() == False:
        print('Deve ser digitado em numeros!')
        continue

    altura = float(altura)
    peso = float(peso)

    imc = peso / (altura*altura)
    print(f'Seu IMC é {imc:.2f}.')

    finalizador = input('Deseja continuar? [S]im ou [N]ão : '.lower())
    if finalizador == 's':
        break
