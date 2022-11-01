print('Modelo de hora do programa 0-23h')
hora = int(input('Digite o horário atual: '))


if hora >= 0 and hora <= 11:
    print('Bom Dia!!')
elif hora >= 12 and hora <= 17:
    print('Boa Tarde!!')
elif hora >= 18 and hora <= 23:
    print('Boa Noite!!')
else:
    print('Digite um horário de 0 a 23 horas!')
