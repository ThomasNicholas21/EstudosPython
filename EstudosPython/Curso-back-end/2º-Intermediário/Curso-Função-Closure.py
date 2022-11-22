"""
Closure e funções que retornam outras funções
"""


def saudacao(mensagem):
    def name(nome):
        return f'{mensagem}, {nome}!'
    return name


falar_bom_dia = saudacao('Bom dia')
falar_boa_tarde = saudacao('Boa tarde')
falar_boa_noite = saudacao('Boa noite')

lista_clientes = ['Thomas', 'Alberto', 'Jubileu']

for nome in lista_clientes:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))
    print()
