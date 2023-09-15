import datetime
anon = int(input('Qual seu ano de nascimento? '))
currentdatetime = datetime.datetime.now()
ano = currentdatetime.date()
year = ano.strftime('20' + '%y')
ano = int(year)
sexo = str(input('Qual seu sexo? '))
difa = ano - anon
if sexo == 'feminino':
        print('Você não precisa se alistar.')
elif sexo == 'masculino':
    if difa < 18:
        print('Você ainda deve se alistar no exército.')
        num1 = 18 - difa
        print('Você tem atualmente {} anos, deve se alistar daqui à {} anos, ou seja,'.format(difa, num1), end='')
        print(' no ano de {}.'.format(anon + 18))
    elif difa == 18:
        print('Você deve se alista no exército esse ano.')
    else:
        num1 = difa - 18
        num2 = anon + 18
        print('Você deveria ter se alistado a {} anos, pois seu ano de alistamento foi {}.'.format(num1, num2))

