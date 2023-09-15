'''num = list()
maior = 0
menor = 0
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para posição {n}: ')))
print('Os números da lista são:', end='')
for x in num:
    print(f' {x}', end='')
print('.')
for a in num:
    if menor == 0:
        maior = menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print(f'O menor número foi {menor} na posição ', end='')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c + 1}', end='...')
print(f'\nO maior número foi {maior} na posição ', end='')
for k, l in enumerate(num):
    if l == maior:
        print(f'{k + 1}', end='...')'''
num = []
mai = 0
men = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('-='*30)
print(num)
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...',end='')
print()