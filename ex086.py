'''matriz = [[], [], []]
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
    print(f'[ {a} ]', end=' ')'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
