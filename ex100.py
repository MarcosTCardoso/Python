from random import randint
from time import sleep


def sorteio(lst):
    print(f'Sorteando os {len(lst)} valores da lista: ', end='')
    for a in range(0, 5):
        aleatório = (randint(1, 10))
        lst.append(aleatório)
    for a in lst:
        print(f'{a} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO')


def somaPar(lst):
    par = 0
    for a in lst:
        if a % 2 == 0:
            par += a
    print(f'Somando os valores pares de {lst}, temos {par}.')


chama = list()
sorteio(chama)
somaPar(chama)
