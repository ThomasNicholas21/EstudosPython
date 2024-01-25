#aplicação closure em calculadora

def calculadora():
    def soma(numero1, numero2):
        return numero1 + numero2
    
    def subratacao(numero1, numero2):
        return numero1 - numero2
    
    def divisao(numero1, numero2):
        return numero1 / numero2
    
    def multiplicacao(numero1, numero2):
        return numero1 * numero2
    
    return {
        'somar': soma,
        'subtrair': subratacao,
        'Dividir': divisao,
        'multiplicar': multiplicacao
    }

calc = calculadora()

numero1 = int(input("Primeiro numero: "))
numero2 = int(input("Segundo numero: "))

operacao = input("Deseja somar, subtrair, dividir ou multiplicar?"
                    "\nSomar - '+'\nSubtrair - '-'\nDividir - '/'\nMultiplicar - 'x'\nDigite: ")

if operacao == '+': 
    print(calc['somar'](numero1, numero2))
elif operacao == '-':
    print(calc['subtrair'](numero1, numero2))
elif operacao == '/': 
    print(calc['dividir'](numero1, numero2))
elif operacao == 'x':
    print(calc['multiplicar'](numero1, numero2))
else:
    print('Operacao invalida')