'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
if len(num) > 3:
    num.insert(7, 0)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4.')
print(num)
print(f'Nessa lista tem {len(num)} elementos.')'''
#valores = list()
#for cont in range(0, 4):
#    valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista!')
a = [2, 3, 4, 7]
b = a[:] #Isso cria uma cópia de a dentro de b
b[2] = 8
print(f'Lista a = {a}')
print(f'Lista b = {b}')