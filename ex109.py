from funCursoEmVid import moedas

p = float(input('Digite um valor: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(f'Aumentando 10% de {moedas.moeda(p)} temos o valor {moedas.aumento(p, 10)}')
print(f'Reduzindo 30% de {moedas.moeda(p)} temos o valor {moedas.reduzindo(p, 30)}')