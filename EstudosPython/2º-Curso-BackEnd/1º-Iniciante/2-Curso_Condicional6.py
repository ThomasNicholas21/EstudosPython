print('Escolha uma opção: ')
op = int(input('1-Soma de 2 numeros\n \
2-Diferenca entre 2 numeros(maior pelo menor)\n \
3-Produto entre dois numeros\n \
4-Divisao entre 2 numeros(denominador nao pode ser zero)\n \
Opcao:'))

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if op == 1:
    valor = num1 + num2
    print(f'A soma dos valores {valor}')
elif op == 2:
    if num1 > num2:
        print(f'O {num1} > {num2}')
    if num2 > num1:
        print(f'O {num2} > {num1}')
elif op == 3:
    prod = num1 * num2
    prod2 = num2 * num1
    print(f'O produto do primeiro pelo segundo: {prod}')
    print(f'O produto do segundo pelo primeiro: {prod2}')
elif op == 4:
    if num1 != 0:
        div = num2 / num1
        print(f'A divisao do segundo pelo primeiro: {div}')
        if num1 == 0:
            print(f'Denominador nao pode ser zero!')
            if num2 != 0:
                div2 = num1 / num2
                print(f'A divisao do segundo pelo primeiro: {div2}')
                if num2 == 0:
                    print(f'Denominador nao pode ser zero!')
