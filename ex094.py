registro = list()
dados = {}
media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('Erro, digite o sexo corretamente.')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    registro.append(dados.copy())
    dados.clear()
    back = ''
    while True:
        back = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if back not in 'SsNn':
            print('Dado errado, tente novamente!')
        else:
            break
    if back == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(registro)} pessoas.')
for m in range(0, len(registro)):
    media = media + registro[m]['idade']
print(f'A média de idade do grupo é {media / len(registro)}.')
print('As mulheres cadastradas foram: ', end='')
for m in registro:
    if m['sexo'] == 'F':
        print(f'{m["nome"]}', end='...')
print()
print('As pessoas com idade acima da média são: ', end='')
for m in registro:
    if m['idade'] > media / len(registro):
        print(f'{m["nome"]}', end='')
print()
