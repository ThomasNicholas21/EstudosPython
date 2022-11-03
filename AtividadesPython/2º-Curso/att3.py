# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Insira seu nome: '))
while len(nome) < 3:
    nome = str(input('Insira um nome com mais de 3 caracteres: '))

idade = int(input('Insira sua idade: '))
while idade < 0 or idade >= 150:
    idade = int(input('Insira uma idade real: '))

salario = float(input('Qual o seu salário: '))
while salario <= 0:
    salario = float(input('Salario deve ser maior do que zero: '))

sexo = str(input('Digite seu sexo, f para feminino e m para masculino : '))
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Digite f para feminino e m para masculino: '))

estado_civil = str(input('Informe seu estado civil;'
                         's para solteiro(a)'
                         'c para casado(a)'
                         'v para viuvo(a)'
                         'd para divorciado(a)'
                         'Digite:'))
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = str(input('Insira as iniciais adequadas: '))
