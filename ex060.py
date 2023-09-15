num = int(input('Digite um número para descobrir o seu fatorial: '))
c = num
f = 1
'''while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1'''
for fac in range(num, 0, -1):
    print('{}'.format(fac), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)