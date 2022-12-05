"""
Usando módulo para conversão de temperatura
"""

from Curso2 import * # Má prática 
import os

while True:
    conversao = input(
        'Digite qual conversão deseja:\n'
        '[1] - Celsius para Fahrenheit\n'
        '[2] - Celsius para Kelvin\n'
        '[3] - Fahrenheit para Celsius\n'
        '[4] - Fahrenheit para Kelvin\n'
        '[5] - Kelvin para Celsius\n'
        '[6] - Kelvin para Fahrenheit\n'
        'Qual deseja: '
    )
    os.system('cls')
    i = (conversao != '1' and conversao != '2' and conversao != '3' and 
    conversao != '4' and conversao != '5' and conversao != '6')
  
    if i:
        print('Digite o número da conversão desejada.')
        continue

    while conversao == '1':
        celsius = input('Digite a temperatura em Celsius: ')

        try: 
            celsius = float(celsius)
            temp = conversao_celsius_fahrenheit(celsius)
            print(f'A temperatura em Fahrenheit é {temp:.2f}.')
            print()
            break

        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue

    while conversao == '2':
        celsius = input('Digite a temperatura em Celsius: ')

        try: 
            celsius = float(celsius)
            temp = conversao_celsius_kelvin(celsius)
            print(f'A temperatura em Fahrenheit é {temp:.2f}.')
            print()
            break

        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue

    while conversao == '3':
        fahrenheit = input('Digite a temperatura em Fahrenheit: ')

        try: 
            fahrenheit = float(fahrenheit)
            temp = conversao_fahrenheit_celsius(fahrenheit)
            print(f'A temperatura em Celsius é {temp:.2f}.')
            print()
            break

        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue

    while conversao == '4':
        fahrenheit = input('Digite a temperatura em Fahrenheit: ')

        try: 
            fahrenheit = float(fahrenheit)
            temp = conversao_fahrenheit_kelvin(fahrenheit)
            print(f'A temperatura em Kelvin é {temp:.2f}.')
            print()
            break
        
        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue

    while conversao == '5':
        kelvin = input('Digite a temperatura em Kelvin: ')

        try: 
            kelvin = float(kelvin)
            temp = conversao_kelvin_celsius(kelvin)
            print(f'A temperatura em Celsius é {temp:.2f}.')
            print()
            break

        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue

    while conversao == '6':
        kelvin = input('Digite a temperatura em Kelvin: ')
        
        try: 
            kelvin = int(kelvin)
            temp = conversao_kelvin_fahrenheit(kelvin)
            print(f'A temperatura em Fahrenheit é {temp:.2f}.')
            print()
            break
        
        except ValueError:
            print('Digite a temperatura em número.')
            print()
            continue

        except Exception:
            print('Erro desconhecido, tente novamente.')
            print()
            continue


    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair is True:
        break
    else:
        os.system('cls')
        continue
    