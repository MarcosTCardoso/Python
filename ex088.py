'''from random import randint
from time import sleep
jogos = []
dados = []
print('-='*30)
print(f'{"Bem vindo à mega-sena":^60}')
print('-='*30)
quantidade = int(input('Quantos jogos vai jogar? '))
for x in range(0, quantidade):
    cont = 0
    while cont != 6:
        var = [randint(0, 60)]
        if var not in dados:
            dados.append(var)
            cont += 1
    dados.sort()
    jogos.append(dados[:])
    del dados[:]
print('-='*30)
for i, x in enumerate(jogos):
    print(f'\nJogo {i + 1}: ', end='')
    for a in x:
        print(f'{a}', end=' ')
    sleep(1)
print('\n\nEsses são seus jogos!')'''
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{"Joga na Mega Sena":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} Jogos ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '-=' * 5)
