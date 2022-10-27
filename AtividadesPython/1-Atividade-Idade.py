# Faça um programa para ler um número
# indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não
# entrará nos cálculos, contém um valor de idade negativa.
# Calcular e imprimir a idade média deste grupo de indivíduos.
# Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSIVEL CALCULAR".
npessoas: int
soma: float
media: float

idade = int(input('Digite as idades: '))

if idade < 0:
    print('IMPOSSIVEL CALCULAR')
else:
    soma = 0
    npessoas = 0
    while idade >= 0:
        soma = soma + idade
        npessoas = npessoas + 1
        idade = int(input('Digite as idades: '))

    media = soma / npessoas
    print(f'{media:.2f}')
