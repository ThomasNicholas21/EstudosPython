#calculadora com função
import os

def soma(n1, n2): 
    soma = n1 + n2 
    return print(soma) 

def subtracao(n1, n2):
    subtracao = n1 - n2 
    return print(subtracao)

def div(n1, n2):
    div = n1 / n2
    if n2 == 0:
        print("Divisao por zero!!!!!") 
    return print(div)

def multiplicacao(n1, n2):
    multiplicacao = n1 + n2 
    return print(multiplicacao)


while True: 
    print("Selecione seus numeros:")
    n1 = float(input("Primeiro Numero: "))
    n2 = float(input("Segundo Numero: "))
    print()

    operador = input("Selecione seu operador:\n"
                        "+ para soma\n"
                        "- para subtracao\n"
                        "x para multiplicacao\n"
                        "/ para divisao\n"
                        "Qual operacao vai realizar: ")
    print()
    
    if operador != "+" and operador != "-" and operador != "x" and operador != "/":
        print("Selecione um operador valido")
        continue    
    else:
        if operador == "+":
            soma(n1, n2)
        elif operador == "-":
            subtracao(n1, n2)
        elif operador == "x":
            multiplicacao(n1, n2)
        elif operador == "/":
            div(n1, n2)

    sair = input("Deseja sair? Resposta: ").lower().startswith("s")
    if sair is True:
        break
    else:
        os.system("cls")
    
    