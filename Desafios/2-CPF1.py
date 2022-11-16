cpf = input('Digite seu CPF: ')
novo_cpf = cpf[:9]
total_soma = 0
reverso = 10

for i in novo_cpf:
    total_soma += int(i) * reverso
    reverso -= 1


multiplicação = total_soma * 10
print(multiplicação)
resto_multiplicação = multiplicação % 11
print(resto_multiplicação)

if resto_multiplicação > 9:
    print('Resultado é 0')
else:
    print('Resultado é o valor da conta.')
