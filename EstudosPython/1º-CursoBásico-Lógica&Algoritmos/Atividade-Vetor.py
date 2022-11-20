""" 
Faça um programa que leia N números reais e armazene-os em um vetor.
Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor

"""
x = int(input('Quantos numeros serao digitados: '))
vet = [0 for l in range(x)]

for i in range(0, x):
    vet[i] = float(input('Digite um numero: '))

print()
for i in range(0, x):
    print(f'Valores: {vet[i]:.2f}')

print()

soma = 0
for i in range(0, x):
    soma = soma + vet[i]

print(f'A soma dos elementos do vetor: {soma}')
media = soma / x
print(f'A media dos elementos do vetor: {media}')
