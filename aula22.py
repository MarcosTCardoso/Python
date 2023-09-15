from funCursoEmVid import moedas

p = float(input('Digite um valor: R$'))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10% temos {moedas.aumento(p, 10)}')
print(f'Diminuindo 30% temos {moedas.reduzindo(p, 30)}')
