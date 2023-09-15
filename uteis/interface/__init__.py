def título(msg):
    print('-' * 50)
    print(f'{msg.upper()}'.center(50))
    print('-' * 50)


def linha(tam=50):
    return print('-' * tam)


def cabeçalho(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')


def opções(msg):
    válido = False
    while not válido:
        try:
            op = int(input(msg))
        except ValueError or op == '' or op not in '123':
            print(f'\033[31mErro! Valor inválido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário não quis informar o valor.')
            return 0
        else:
            if str(op) in '1 2 3':
                return op



