'''print('='*50)
print('{:^50}'.format('Bem-vindo à Caixa'))
print('='*50)
valor = int(input('Qual o valor será sacado? R$ '))
cont = valor
while True:
    result = valor // 50
    resto = (valor - result * 50)
    result2 = resto // 20
    resto2 = valor - (result * 50 + result2 * 20)
    result3 = resto2 // 10
    resto3 = valor - (result * 50 + result2 * 20 + result3 * 10)
    result4 = resto3 // 1
    print(f'''#Total de {result} cédulas de R$ 50,00
    #Total de {result2} de cédulas R$ 20,00
    #Total de {result3} cédulas de R$ 10,00
    #total de {result4} cédulas de R$ 1,00''')
    #break'''
print('='*50)
print('{:^50}'.format('Bem-vindo à Caixa'))
print('='*50)
valor = int(input('Qual o valor será sacado? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*50)
print('Volte sempre!')