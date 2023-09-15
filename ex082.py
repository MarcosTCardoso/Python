'''num = list()
numi = list()
nump = list()
while True:
    numu = int(input('Digite um número para ser analisado: '))
    num.append(numu)
    if numu % 2 == 0:
        nump.append(numu)
    else:
        numi.append(numu)
    while True:
        back = str(input('Você deseja sair do programa [S/N]? ')).strip().upper()[0]
        if back in 'SsNn':
            break
    if back == 'S':
        break
print(f'Os números digitados foram {num}.\nOs ímpares são {numi}.\nOs pares são {nump}')'''
num = list()
while True:
    num.append(int(input('Digite um valor para ser analisado: ')))
    while True:
        back = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if back in 'SsNn':
            break
    if back == 'N':
        break
numi = list()
nump = list()
for a in num:
    if a % 2 == 0:
        numi.append(a)
    else:
        nump.append(a)
print(f' A lista completa é {num}. \n')
