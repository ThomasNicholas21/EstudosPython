estado = int(input('Digite seu o numero do seu estado para calculo da taxa de imposto:\n \
1-MG - 7%\n 2-SP - 12%\n 3-RJ - 15%\n 4-MS - 8%\n Selecione:'))
ValorProd = float(input('Digite o valor do produto: '))

if estado == 1:
    ValorFinal = ValorProd + ValorProd*0.07
    print(f'O valor do produto fica: {ValorFinal}')
elif estado == 2:
    ValorFinal = ValorProd + ValorProd*0.12
    print(f'O valor do produto fica: {ValorFinal}')
elif estado == 3:
    ValorFinal = ValorProd + ValorProd*0.15
    print(f'O valor do produto fica: {ValorFinal}')
elif estado == 4:
    ValorFinal = ValorProd + ValorProd*0.08
    print(f'O valor do produto fica: {ValorFinal}')
else:
    print('Não possuimos entregas para esse estado.')
