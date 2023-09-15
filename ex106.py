'''def leiaInt(n=''):
    while True:
        if n.isnumeric():
            print(f'Você digitou o valor {n}.')
            break
        else:
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')


s = str(input('Digite um número inteiro: '))
leiaInt(s)'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Erro! Digite um valor inteiro válido.')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
