'''from random import randint
tup = (randint(0, 5), randint(0, 5), randint(0, 5),
       randint(0, 5), randint(0, 5))
menor = 0
maior = 0
cont = 0
while cont != 5:
    for i in tup:
        if cont == 0:
            menor = i
            maior = i
        else:
            if menor > i:
                menor = i
            if maior < i:
                maior = i
    cont += 1
print(f'Os números gerados foram {tup}, o menor é {menor} e o maior é {maior}.')'''
from random import randint
tup = (randint(0, 5), randint(0, 5),randint(0, 5),
       randint(0, 5), randint(0, 5))
print('Os valores sorteados foram: ', end='')
for i in tup:
    print(f'{i}', end=' ')
print(f'\nO maior valor foi {max(tup)}.')
print(f'O menor valor foi {min(tup)}.')
