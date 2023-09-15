'''ti = int(input('Qual o termo inicial? '))
razao = int(input('Qual a razão? '))
termo = ti
cont = 0
fix = 10
giro = False
while cont <= fix:
    print('{}'.format(termo), end='')
    termo += razao
    print(' --> ' if cont <= 9 else '', end='')
    cont += 1
    if cont == fix:
        fi = int((input('\nQuantos termos quer saber a mais? ')))
        fix += fi
        print(end='')
        if fi == 0:
            giro = True
print('pausa')
'''
ti = int(input('Qual o termo inicial? '))
razao = int(input('Qual a razão? '))
termo = ti
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pause')
    mais = int(input('Quantos você quer saber a mais? '))
print('Você visualizou o total de {} termos na PA.'.format(total))
