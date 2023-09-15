'''print('\033[31m-=-\033[m' * 30)
print('{:^90}'.format('Bem-vindo à calculadora de TABUADAS.'))
print('\033[31m-=-\033[m' * 30)
tab = int(input('Digite o número que deseja saber a tabuada: '))
fix = list(range(1, 10 + 1))
for c in range(1):
    print(' {} X {} é {}'.format(fix[0], tab, (tab * 1)))
    print(' {} X {} é {}'.format(fix[1], tab, (tab * 2)))
    print(' {} X {} é {}'.format(fix[2], tab, (tab * 3)))
    print(' {} X {} é {}'.format(fix[3], tab, (tab * 4)))
    print(' {} X {} é {}'.format(fix[4], tab, (tab * 5)))
    print(' {} X {} é {}'.format(fix[5], tab, (tab * 6)))
    print(' {} X {} é {}'.format(fix[6], tab, (tab * 7)))
    print(' {} X {} é {}'.format(fix[7], tab, (tab * 8)))
    print(' {} X {} é {}'.format(fix[8], tab, (tab * 9)))
    print('{} X {} é {}'.format(fix[9], tab, (tab * 10)))'''
tabuada = int(input('Digite o número que deseja saber a tabuada: '))
for c in range(0, 11):
    print('{} X {} = {}.'.format(tabuada, c, tabuada * c))