
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao
def preenchedor_5(*args):
    args = []
    for i in range(5):
        armazenamento = input('Digite seus valores: ')
        e_string(armazenamento)
        armazenamento = int(armazenamento)
        args.append(armazenamento)
    return args
    
@criar_funcao
def preenchedor_7(*args):
    args = []
    for i in range(7):
        armazenamento = input('Digite seus valores: ')
        e_string(armazenamento)
        armazenamento = int(armazenamento)
        args.append(armazenamento)
    return args

def e_string(parametro):
    try: 
        parametro = int(parametro)
    except:
        raise ValueError('insira um Numero')
    return parametro