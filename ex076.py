'''listagem = ('Notebook', 4000,  'Pão', 1, 'Abobrinha', 2.50, 'Feijão', 5.50, 'Arroz', 11, 'Mochila', 25.50)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
#cont = 0
for cont in range(0, len(listagem), 2):
    calc = len(listagem[0])
    calcc = str(41 - calc)
    format1 = '{:.<' + calcc + '} R$'
    ind = cont + 1
    print(format1.format(listagem[cont]), '{:>8}'.format(float(listagem[ind])))'''
listagem = ('Notebook', 4000,
            'Pão', 1,
            'Abobrinha', 2.50,
            'Feijão', 5.50,
            'Arroz', 11,
            'Mochila', 25.50)
print('-'*40)
print(f'{"LISTA DE ITENS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')