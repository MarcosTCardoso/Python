'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 120
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')'''
for e in brasil:
    for v in e.values():
        print(f'{v}')
print(brasil)
