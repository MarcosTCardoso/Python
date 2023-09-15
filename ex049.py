s = 0
cont = 0
resp = '0'
for c in range(1, 7):
    n = int(input('Digite o numero: '))
    ta = n % 2
    if ta == 0:
        s += n
        cont += 1
    if cont > 1:
        resp = 'números pares inseridos'
    if cont == 1:
        resp = 'número par inserido '
print('A soma de {} {}é {}.'.format(cont, resp, s))
print('Fim')