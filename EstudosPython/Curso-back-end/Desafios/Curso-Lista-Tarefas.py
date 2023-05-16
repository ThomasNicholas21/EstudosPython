import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa listada.')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer():
    print('Tarefa desfeita.\n')
    return tarefas_desfazer.append(tarefas.pop())

def refazer():
    print('Tarefa restaurada.\n')
    return tarefas.append(tarefas_desfazer.pop())

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Isso não é uma tarefa.')
        return
    
    tarefas.append(tarefa)

CAMINHO_ARQUIVO = 'Curso-Lista-Tarefas.py'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_desfazer = []

while True:

    print('Comandos: Listar, desfazer, refazer e sair.')
    op = input('Digite a tarefa ou comando: ').lower()

    comandos = {
        'listar' : lambda: listar(tarefas),
        'desfazer' : lambda: desfazer(),
        'refazer' : lambda: refazer(),
        'adicionar' : lambda: adicionar(op, tarefas),
    }

    comando = comandos.get(op) if comandos.get(op) is not None else \
        comandos['adicionar']
    comando()

    if op == 'sair':
        break
    
    salvar(tarefas, CAMINHO_ARQUIVO)
    # if op.isdigit():
    #     print('Isso não é uma tarefa.')
    #     print()
        
    # elif op == 'listar':
    #     listar(tarefas)
        
    # elif op == 'desfazer':
    #     desfazer()

    # elif op == 'refazer':
    #     refazer()

    if op == 'sair':
        break
    
    # else:
    #     adicionar(op, tarefas)