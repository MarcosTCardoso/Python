ti = int(input('Digite o termo inicial da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = (ti + razao) * 5
pa = ti
while pa < cont:
    pa += razao
    print('{}'.format(pa), end='')
    print(' --> ' if pa < cont else '', end='')