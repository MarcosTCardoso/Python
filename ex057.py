'''sexo = ''
cont = 0
while sexo != 'M' and sexo != 'F':
    if cont == 0:
        sexo = str(input('Sexo [M/F]:'.upper()))
        cont = 1
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('O dado inserido é inválido. Digite o sexo: ').upper())
print('Dado inserido com sucesso.')'''
sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Por favor, informe seu sexo: '))
print('Sexo {} registrado com sucesso.'.format(sexo))