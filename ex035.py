numero = int(input('Digite um número inteiro para ser convertido: '))
print('Digite o número da conversão que deseja, seguindo a seguinte ordem: ')
print('[ 1 ] converter para BINÁRIO.')
print('[ 2 ] converter para OCTAL.')
print('[ 3 ] converter para HEXADECIMAL.')
request = int(input('Digite a opção desejada: '))
calc = 0
if request == 1:
    print('O {} convertido para BINÁRIO é o valor de {}.'.format(numero, bin(numero)[2:]))
elif request == 2:
    print('O {} convertido para OCTAL é o valor de {}.'.format(numero, oct(numero)[2:]))
elif request == 3:
    print('O {} convertido para HEXADECIMAL é o valor de {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, digite novamente.')