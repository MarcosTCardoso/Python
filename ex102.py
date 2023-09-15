def fatorial(n, show=False):
    """

    :param n: Número que se calculará o fatorial.
    :param show: Se True vai mostrar a conta, se false ou não informado não mostra.
    :return: Retorna o fatorial do número inteiro n.

    """
    f = 1
    print('-' * 60)
    for num in range(n, 0, -1):
        if show:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
        f *= num
    return f


print(fatorial(7, True))
help(fatorial)
