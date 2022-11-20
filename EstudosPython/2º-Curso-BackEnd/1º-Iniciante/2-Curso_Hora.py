"""
Atividade Horas
"""
print('Modelo de horário: 0h - 23h')
hora = input('Digite o horário: ')

try:
    hora = hora(int)
    hora1 = hora >= 0 and hora <= 11
    hora2 = hora >= 12 and hora <= 17
    hora3 = hora >= 18 and hora <= 23
    if hora1:
        print(f'Bom dia, são {hora}h')
    elif hora2:
        print(f'Boa tarde, são {hora}h')
    elif hora3:
        print(f'Boa noite, são {hora}h')
    else:
        print('Desculpe, modelo de hora errado.')

except:
    print('Digite a hora com números.')
