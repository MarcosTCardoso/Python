sequencia = int(input('Digite até onde quer ver a sequência fibonacci: '))
t1 = 0
t2 = 1
cont = 0
t3 = t1 + t2
print('{} - {}'.format(t1, t2), end=' - ')
while cont <= sequencia - 2:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end='')
    print(' - ' if cont < sequencia - 2 else '', end='')
    cont += 1