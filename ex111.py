from funCursoEmVid import dados, moedas

p = dados.leiaDinheiro('Qual o valor do produto? R$')
print(moedas.resumo(p, 10, 15))