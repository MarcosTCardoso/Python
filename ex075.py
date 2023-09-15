'''tup = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'Você digitou {tup}')
nine = tup.count(9)
if nine > 0:
    print(f'O número 9 apareceu {nine} vezes.')
else:
    print('O número 9 não apareceu.')
position = tup.count(3)
treePosition = 0
if position >= 1:
    treePosition = tup.index(3)
    if treePosition >= 0:
        print(f'O número 3 apareceu na posição {position + 1}')
else:
    print('Não há número 3 na tupla.')
par = 0
cont = 0
print('São pares os números: ', end='')
while cont != 1:
    for i in tup:
        if i % 2 == 0:
            print(f'{i} ', end='')
    cont += 1'''
tup = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'Você digitou {tup}.')
print(f'Você digitou o número 9 {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3)+1}ª posição.')
else:
    print('Não há 3 nessa tupla.')
print('Os números pares são: ', end='')
for n in tup:
    if n % 2 == 0:
        print(f'{n}', end=' ')