def operador(x, y, o):
    if o == "1":
        return x+y
    elif o == "2":
        return x - y
    elif o == "3":
        return x / y
    else:
        return x * y


while True:
    try:
        num1 = float(input('Insira um número: '))
        num2 = float(input('Insira um número: '))

        op = input(
            'Opçoes\n'
            '[1] - Soma\n'
            '[2] - Subtracao\n'
            '[3] - Divisao\n'
            '[4] - Multiplicacao\n'
            'Opções:'
        )

        value = operador(num1, num2, op)
        print(value)

    except ((TypeError, ValueError)):
        print('Erro: Valor errado')
        print()

    except ZeroDivisionError:
        print('Erro: Divisao por zero')
        print()

    except Exception:
        print('Erro desconhecido')
        print()

    sair = input('Deseja sair: [s]im e [n]ao: ').lower().startswith('s')
    if sair is True:
        break
    print()
