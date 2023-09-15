from random import randint
print('=-'*50)
print('{:^100}'.format('Vamos jogar Par ou Impar!'))
print('=-'*50)
cont = 0
while True:
    usuario = int(input('\nDigite um número: '))
    cuser = str(input('Digite PAR ou IMPAR: ')).strip().upper()
    computador = randint(0, 10)
    soma = usuario + computador
    result = ''
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    if cuser == result:
        print('-'*20)
        print(f'Parabéns, o resultado foi {result}.')
    else:
        break
    cont += 1
    print(f'Você jogou {usuario} o computador jogou {computador}.\n' + '-'*20, end='')
print(f'O computador jogou {computador} e você {usuario}. Logo o número é {result}.\nVocê ganhou {cont} vezes do computador.')