cont = acum = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    acum += num
print(f'A soma dos {cont} números é {acum}.')