"""
Utilizando o Range
"""

while True:
    stop = input('Digite até onde deseja contar seu numero: ')
    step = input(
                'Digite como deseja a a forma que seus numeros sejam contados: '
                '\nExemplo: de 2 em 2 ou de 3 em 3 \n'
                '\nComo deseja: '
                )

    try:            
        stop_int = int(stop)
        step_int = int(step)

        for i in range(0, stop_int, step_int):
            print(f'{i}')

    except:
        print('Deve-se digitar apenas números!')
        continue
    
    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair == True:
        break