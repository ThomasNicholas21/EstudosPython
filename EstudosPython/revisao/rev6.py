#Função que retorna se o número é par ou não

def validador(param):
    if param % 2 == 0:
        return print(f"Valor '{param}' é par")
    return print(f"Valor '{param}' é impar")

try:
    numero = int(input("Digite um número: "))
    print("\nProcessando número ...\n")
    validador(numero)

except:
    print("O valor não é número!")