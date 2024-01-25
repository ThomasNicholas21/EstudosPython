#calculadora simples

operador = input("Selecione operadores:\n"
        "+ para soma\n"
        "- para subtracao\n"
        "x para multiplicacao\n"
        "/ para divisao\n"
        "Selecione:")

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if operador == "+":
    soma = n1 + n2
    print(soma)

elif operador == "-":
    subtracao = n1 - n2
    print(subtracao)

elif operador == "x":
    mult = n1 * n2
    print(mult)

elif operador == "/":
    div = n1 / n2
    print(div)

else: 
    print("Operador invalido")