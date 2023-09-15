n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        if n % 2 != 0:
            impares += 1
print('Foram {} pares e {} impares. \nAcabou.'.format(pares, impares))