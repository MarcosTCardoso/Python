idm = 0
oldm = 'name'
holdm = 0
mulher = 0
for c in range(1, 5):
    print('----{}ª Pessoa----'.format(c))
    name = str(input('Qual o nome? '))
    old = int(input('Qual a idade? '))
    sex = str(input('Sexo [M/F]: '))
    idm = idm + old / 4
    if sex == 'M':
        if old > holdm:
            holdm = old
            oldm = name
    elif sex == 'F' and old < 20:
        mulher = mulher + 1
print('''Idade média: {}.
Homem mais velho: {}. 
Mulheres com menos de 20 anos: {}.'''.format(idm, oldm, mulher))
