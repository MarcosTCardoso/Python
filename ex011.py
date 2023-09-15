'''dat = int(input('Qual ano você está? '))
datp = dat % 4
if datp == 0:
    print('O ano {} é um ano Bissexto.'.format(dat))
else:
    print('O ano {} não é Bissexto.'.format(dat))'''
from datetime import date
print('-=-' * 21)
print('   ' * 9 + 'Bem-vindo!' + '   ' * 5)
print('-=-' * 21)
dat = int(input('Qual o  ano você quer analisar? Digite 0 para análise do ano atual. \n'))
if dat == 0:
    dat = date.today().year
if dat % 4 == 0 and dat % 100 != 0 or dat % 400 == 0:
    print('O ano de {} é bissexto.'.format(dat))
else:
    print('O ano de {} não é bissexto.'.format(dat))
