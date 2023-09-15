'''from time import sleep
boletim = []
dados = []
individual = 0
while True:
    nome = str(input('Nome: '))
    nota = [float(input('Nota 1: ')), float(input('Nota 2: '))]
    media = (nota[0] + nota[1]) / 2
    dados.append(nome)
    dados.append(nota)
    dados.append(media)
    boletim.append(dados[:])
    del dados[:]
    back = ''
    while True:
        back = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if back in 'SsNn':
            break
    if back == 'N':
        break
print('-='*30)
print(f'{"Boletim da Turma":^60}')
print('-='*30)
for i, x in enumerate(boletim):
    print(f'{i:<5}', end='')
    print(f'{x[0]:<45}', end='')
    print(f'{x[2]:>10}')
print('-'*60)
while True:
    individual = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if individual == 999:
        break
    else:
        print(f'As notas de {boletim[individual][0]} são {boletim[individual][1]}')
print('CARREGANDO...')
sleep(2)
print('-'*60)
print(f'{"OBRIGADO POR USAR O CMD":^60}')'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são: {ficha[opc][1]}.')


