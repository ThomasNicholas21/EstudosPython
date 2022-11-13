"""
Utilizando o Range
"""

from tracemalloc import start


while True:
    start = input('Digite aonde deseja começar a fazer sua contagem: ')
    stop = input('Digite até onde deseja contar seu numero: ')
    step = input(
                'Digite como deseja a a forma que seus numeros sejam contados: '
                '\nExemplo: de 2 em 2 ou de 3 em 3 '
                '\nComo deseja: '
                )
    cont = 0

    try:            
        stop_int = int(stop)
        step_int = int(step)
        start_int = int(start)

        print(
                f'Forma selecionada de {step_int} em {step_int}.'
                f'\nE será contado de {start_int} até {stop_int}.'
            )
        for i in range(start_int, stop_int, step_int):
            cont += 1
            print(f'{cont}º número = {i}')

    except:
        print('Deve-se digitar apenas números!')
        continue
    
    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair == True:
        break