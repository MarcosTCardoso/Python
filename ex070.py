'''print('-'*50)
print('{:^50}'.format('Bem-vindo!'))
print('{:^50}'.format('Vamos calcular o valor dos produtos.'))
print('-'*50)
total = caro = 0
produto = ''
prodv = 0
cont = 0
while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Valor do Produto: '))
    continuar = str(input('Você deseja continuar? ')).strip().upper()[0]
    print('-'*50)
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja continuar? '))
    total += valor
    if valor > 1000:
        caro += 1
    if cont == 0:
        produto = nome
        prodv = valor
    if valor < prodv:
        produto = nome
        prodv = valor
    cont += 1
    if continuar == 'N':
        break
print(f'Você gastou R$ {total:.2f}, haviam {caro} produtos que custavam mais de R$ 1000,00. O produto mais barato foi {produto}.')
'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total foi R$ {total:.2f}')
print(f'Temos {totmil} custando mais de R$ 1.000,00.')
print(f'O produto mais barato custa R$ {menor:.2f}.')
