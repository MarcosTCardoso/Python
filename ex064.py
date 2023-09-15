cont = acum = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    acum += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números, o resultado é {}.'.format(cont, acum))