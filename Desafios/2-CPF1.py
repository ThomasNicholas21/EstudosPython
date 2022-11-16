cpf = input('Digite seu CPF: ')
novo_cpf = cpf[:9]
total_soma = 0
reverso1 = 10

for i in novo_cpf:
    total_soma += int(i) * reverso1
    reverso1 -= 1

digito_1 = (total_soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)
