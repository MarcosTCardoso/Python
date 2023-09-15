cont = acum = maior = menor = media = 0
'''continuar = False
while not continuar:'''
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    conti = str(input('Quer continuar? [S/N]')).upper()
    if cont == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    acum += num
    media = acum / cont
    if conti == 'N':
        '''continuar = True'''
        continuar = 'N'
    while conti != 'S' and conti != 'N':
        conti = str(input('Opção inválida. Quer continuar? [S/N]: ')).upper()
        if conti == 'N':
            continuar = conti
print('A média entre esses valores é {}, o menor número é {} e o maior é {}.'.format(media, menor, maior))