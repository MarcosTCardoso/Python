'''num = list()
cont = 0
while cont != 5:
    user = int(input('Digite um valor: '))
    if cont == 0:
        num.append(user)
        print('Esse valor foi adicionado ao fim da lista.')
    elif user in num:
        while True:
            user = int(input('Valor já consta. Digite novamente: '))
            if user not in num:
                for a in num:
                    if user < num[a]:
                        num.insert(a, num)
                        print(f'O valor foi adicionado na posição {num.index(a)} na lista.')
                break
    else:
        for a in num:
            if user < num[a]:
                num.insert(a, num)
                print(f'O valor foi adicionado na posição {num.index(a)} na lista.')
    cont += 1
print(num)'''
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print('-='*30)
print(f'Os valore digitados em ordem foram {lista}')
