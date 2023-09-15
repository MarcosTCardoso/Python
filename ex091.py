from random import randint
from time import sleep
from operator import itemgetter
valores = {}
cont = 0
print('A jogada dos jogadores é: ')
for a in range(0, 4):
    valores[f'jogador {a + 1}'] = randint(1, 6)
ranking = list()
for i, j in valores.items():
    print(f'    {i}: {j}')
    sleep(0)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('O ranking ficou assim: ')
for i, v in enumerate(ranking):
    print(f'    Em {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
