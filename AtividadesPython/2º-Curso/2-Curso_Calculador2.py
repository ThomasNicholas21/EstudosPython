"""
Calculadora
"""

while True:
    num1 = input('Digite o primeiro numero: ')
    num2 = input('Digite o segundo numero: ')
    print("Operadores:       "
          "\n + = soma          "
          "\n - = subtração     "
          "\n / = divisão       "
          "\n * = multiplicação ")
    operador = input('Selecione seu operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Deve ser digitados numeros!')
        continue

    num1 = float(num1)
    num2 = float(num2)

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador: ')
        continue

    if operador == '+':
        print('Soma = ', num1 + num2)
    elif operador == '-':
        print('Subtração = ', num1 - num2)
    elif operador == '/':
        print('Divisão = ', num1 / num2)
    else:
        print('Multiplicação = ', num1 * num2)

    sair = input('Deseja sair: [s]im ou [n]ão').lower().startswith('s')

    if sair is True:
        break
