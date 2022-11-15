"""
desempacotamento de listas
"""

while True:
    dados_armazenados = []
    dado1 = input('Digite seu nome: ')
    dados_armazenados.append(dado1)
    dado2 = input('Digite sua cidade natal: ')
    dados_armazenados.append(dado2)
    dado3 = input('Digite seu desenho favorito: ')
    dados_armazenados.append(dado3)
       
    print(dados_armazenados)

    dado1, dado2, dado3 = dados_armazenados

    deseja_retirar_algum_dado = input('Sim ou Não : ').lower().startswith('s')
    if deseja_retirar_algum_dado is True:
        qual_dado = input(
                            'Qual dado deseja retirar: '
                            f'\n{dado1}'
                            f'\n{dado2}'
                            f'\n{dado3}'
                            '\nQual deseja: '
                        )
        if qual_dado == dado1:
            dados_armazenados.pop(dado1)
        elif qual_dado == dado2:
            dados_armazenados.pop(dado2)
        else:
            dados_armazenados.pop(dado3)

    print(dados_armazenados)

    sair = input('Sair? [S]im ou [N]ão: ').lower().startswith('s')
    if sair is True:
        break

   

    
  
       