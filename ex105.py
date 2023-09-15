from time import sleep

c = ('\033[m',         # 0 - Sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - Amarelo
     '\033[1;39;44m',  # 4 - Azul
     '\033[0;30;45m',  # 5 - Roxo
     '\033[1;39;40m'   # 6 - Branco
     )


def título(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * (tam + 8))
    print(f'    {msg}')
    print('~' * (tam + 8))
    print(c[0], end='')


def ordem(fun=''):
    título(f'Acessando o manual do comando {fun}', 4)
    sleep(2)
    print(c[6], end='')
    help(fun)
    print(c[0], end='')


s = ''
while True:
    título('Bem vindo ao sistema PyHelp', 2)
    s = str(input('Função ou Biblioteca > ')).strip()
    if s.upper() == 'FIM':
        break
    ordem(s)
título('Até logo.', 1)
