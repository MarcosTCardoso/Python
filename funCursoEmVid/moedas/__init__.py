def metade(n, f=True):
    r = n / 2
    return r if f is False else moeda(r)


def dobro(n, f=True):
    r = n * 2
    return r if f is False else moeda(r)


def aumento(n, p, f=True):
    r = (n * (p / 100)) + n
    return r if f is False else moeda(r)


def reduzindo(n, p, f=True):
    r = n - (n * (p / 100))
    return r if f is False else moeda(r)


def moeda(n=0.0, moeda='R$'):
    x = f'{moeda}{n:.2f}'.replace('.', ',')
    return x


def resumo(num, aum, dim):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num)}')
    print(f'Metade do preço: \t{metade(num)}')
    print(f'{aum}% de aumento: \t{aumento(num, 80)}')
    print(f'{dim}% de redução: \t{reduzindo(num, 35)}')
