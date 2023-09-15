pre = float(input('Qual o preço do produto? '))
print('FORMAS DE PAGAMENTO: ')
print('[ 1 ] à vista dinheiro.')
print('[ 2 ] à vista cartão.')
print('[ 3 ] 2X no cartão.')
print('[ 4 ] 3X ou mais.')
con = str(input('Qual a condição de pagamento? '))
if con == '1':
    print('O preço do produto é de R$ {:.2f}.'.format(pre - pre * (10 / 100)))
elif con == '2':
    print('O preço do produto é de R$ {:.2f}.'.format(pre - pre * (5/100)))
elif con == '3':
    print('o preço do produto é de R$ {:.2f}.'.format(pre))
elif con == '4':
    parcelas = int(input('Será dividido em quantas parcelas? '))
    val = (pre + (pre * 0.2)) / parcelas
    pref = pre + (pre * 0.2)
    print('O produto parcelado em {}X, terá uma parcela de R$ {:.2f},'.format(parcelas, val), end='')
    print(' custando ao final o valor de R$ {:.2f}.'.format(pref))