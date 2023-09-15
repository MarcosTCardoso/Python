'''def somar(a = 0, b = 0, c = 0):

    -> Faz a soma dos termos introduzidos e mostra o resultado na tela:
    :param a: Termo inicial.
    :param b: Termo final.
    :param c: Razão da progressão.
    :return: Sem retorno.

    s = a + b + c
    print(f'O resultado é {s}.')


somar(5, 6, 11)
help(somar)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(4, 5, 7)
r2 = somar(4, 5)
r3 = somar(4)
print(f'Os valores são {r1}, {r2} e {r3}.')
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores são {f1}, {f2} e {f3}.')'''


def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print('É par!')

print(par(n))