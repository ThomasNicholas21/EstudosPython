# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor
# seja inválido e continue pedindo
# até que o usuário informe um valor válido.

while True:
    print('Insira um valor de zero a dez!')
    a = int(input('Insira um valor: '))

    if a >= 0 and a <= 10:
        print(f'O valor {a} esta valido!')
        break
    else:
        print('Valor invalido!')
