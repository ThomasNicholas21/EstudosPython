'''
Operador ternário
'''

while True:
    idade = int(input('Digite sua idade:'))
    maior_de_idade = (idade >= 18)
    msg = 'Maior de idade' if maior_de_idade else 'Menor de idade'
    print(msg)

    if maior_de_idade:
        break
