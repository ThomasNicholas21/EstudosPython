"""
Usando dir, hasattr e getattr
"""
string = 'Thomas'
metodo = 'strip'

# hasattr checa se um determinado
# objeto tem determinado nome la dentro
if hasattr(string, metodo):
    print('Existe upper')
    # getattr mostra o metodo usado
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
