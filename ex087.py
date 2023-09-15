'''
matriz = [[], [], []]
pares = 0
col3 = 0
mai2 = 0
for n in range(0, 3):
    matriz[0].append(int(input(f'Digite o valor para posição [0:{n}]: ')))
for n in range(0, 3):
    matriz[1].append(int(input(f'Digite o valor para posição [1:{n}]: ')))
for n in range(0, 3):
    matriz[2].append(int(input(f'Digite o valor para posição [2:{n}]: ')))
print('-='*30)
for a in matriz[0]:
    print(f'[ {a} ]', end=' ')
print()
for a in matriz[1]:
    print(f'[ {a} ]', end=' ')
print()
for a in matriz[2]:
    print(f'[ {a} ]', end=' ')
print()
print('-='*30)
for a in matriz:
    for b in a:
        if b % 2 == 0:
            pares += b
    col3 = col3 + a[2]
mai2 = matriz[1][0]
for x in matriz[1]:
    if x > mai2:
        mai2 = x
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da coluna 3 é {col3}.')
print(f'O maior valor da segunda linha é {mai2}.')
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col3 = mai2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para posição [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-=' * 30)
for n in matriz[1]:
    if mai2 == 0 or n > mai2:
        mai2 = n
for l in matriz:
    col3 += l[2]
print(f'A soma dos valores pares é {par}.')
print(f'A soma da coluna 3 é {col3}.')
print(f'O maior número da linha 2 é {mai2}.')

