from funCursoEmVid import moedas

p = float(input('Digite um valor: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10% de {moedas.moeda(p)} temos o valor {moedas.moeda(moedas.aumento(p, 10))}')
print(f'Reduzindo 30% de {moedas.moeda(p)} temos o valor {moedas.moeda(moedas.reduzindo(p, 30))}')
