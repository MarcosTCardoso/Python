from uteis import options

while True:
    options.título('menu principal')
    options.cabeçalho(['Mostrar pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    options.linha(50)
    op = options.opções('Sua opção: ')
    if op == 1:
        print(options.título('Opção 1'))
    elif op == 2:
        print(options.título('Opção 2'))
    elif op == 3:
        print(options.título('Até logo! Volte sempre.'))
        break
    else:
        break
