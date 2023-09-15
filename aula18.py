'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[2][1])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''
galera = []
dado = []
for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print('-='*30)
    galera.append(dado[:])
    dado.clear()
print(galera)
mai = men = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        men += 1

print(f'O total de maiores é {mai} e o total de menores é {men}.')

