print('-'*20)
print('{:^20}'.format('Cadastro de Pessoas!'))
print('-'*20)
pessoas = homens = mulheres = 0
while True:
    idade = int(input('IDADE: '))
    sex = str(input('SEXO [F/M]: ')).strip().upper()[0]
    while sex not in 'MmFf':
        sex = str(input('SEXO [F/M]: '))
    continuar = 'sim'
    print('-' * 20)
    while continuar not in 'SsNn':
        continuar = str(input('Você quer continuar? ')).strip().upper()[0]
    if idade > 18:
        pessoas += 1
    if sex == 'M':
        homens += 1
    if sex == 'F' and idade < 20:
        mulheres += 1
    if continuar == 'N':
        break
print(f'Foram cadastrados {pessoas} com mais de 18 anos, {homens} homens e {mulheres} mulheres com menos de 20 anos.')
