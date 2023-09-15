pessoas = []
dados = []
mai = []
men = []
cont1 = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    cont1 += 1
    while True:
        back = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if back in 'SsNn':
            break
    if back == 'N':
        break
cont = 0
for p in pessoas:
    if cont == 0:
        mai.append(p)
        men.append(p)
        cont += 1
    else:
        if p[1] > mai[0][1]:
            del mai[:]
            mai.append(p)
        elif p[1] < men[0][1]:
            del men[:]
            men.append(p)
        elif p[1] == mai[0][1]:
            mai.append(p)
        elif p[1] == men[0][1]:
            men.append(p)
print('-='*30)
print(f'Ao todo você cadastrou {cont1} pessoas.')
print(f'O maior peso foi {mai[0][1]:.2f}. São os mais pesados: ', end='')
for p in range(0, len(mai)):
    print(f'{mai[p][0]}', end=' ')
print(f'\nO menor peso foi {men[0][1]:.2f}. São os mais leves: ', end='')
for p in range(0, len(men)):
    print(f'{men[p][0]}', end=' ')
