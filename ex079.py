'''num = list()
cont = 0
while True:
    if cont == 0:
        num.append(int(input('Digite um número para adicionar: ')))
    elif cont > 0:
        num.append(int(input('Digite um número para adicionar: ')))
    while True:
        if num[-1] in num[0:-1]:
            del num[-1]
            num.append(int(input('Número já registrado, digite novamente: ')))
        else:
            break
    while True:
        conti = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
        if conti in 'SsNn':
            break
    if conti == 'N':
        break
    cont += 1
correct = num.sort()
print('-='*20)
print(f'Você escreveu os números : ', end='')
for p in num:
    print(f'{p}', end=' ')'''
num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    stop = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if stop in 'Nn':
        break
num.sort()
print(f'Você digitou os seguintes números: {num}')
