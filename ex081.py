num = list()
while True:
    num.append(int(input('Digite um número para análise: ')))
    if num[0] == num[-1:0:-1]:
        del num[-1]
        num.append(int(input('Número já consta na lista. Digite novamente: ')))
    while True:
        back = str(input('Você deseja sair [S/N]: ')).strip().upper()[0]
        if back in 'SsNn':
            break
    if back == 'S':
        break
print(f'Foram digitado {len(num)} termos na lista.')
na = num.sort(reverse=True)
print(f'A lista digitada foi ', end='')
for a in num:
    print(f'{a}', end=' ')
if 5 in num:
    print(f'\nA lista possui o número 5 digitado na posição {num.index(5) + 1}.')
else:
    print('\nEssa lista não possui número 5 digitado.')
