jogadores = list()
jogador = dict()
while True:
    print('-=' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for n in range(0, partidas):
        gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {n}? '))
        jogador['gols'].append(gol)
    jogador['Total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    back = ''
    while True:
        back = str(input('Você deseja sair? [S/N] ')).strip().upper()[0]
        if back in 'SsNn':
            break
        print('Valor inválido!')
    if back == 'S':
        break
print('-=' * 30)
print(f'{"COD":<5}', f'{"NOME":<10}', f'{"GOLS":<20}', f'{"TOTAL":>4}')
print('-' * 44)
for i, v in enumerate(jogadores):
    a = str(jogadores[i]['gols'])
    print(f'{i:<5}', f'{v["nome"]:<10}', f'{a:<20}', f'{v["Total"]:>4}')
print('-=' * 30)
while True:
    individual = int(input('Quer saber detalhes de qual jogador? (999 encerra o programa) '))
    if individual == 999:
        break
    else:
        if individual > len(jogadores) - 1:
            print('Erro jogador não cadastrado! Tente novamente.')
        else:
            print(f'-- LEVANTAMENTO DO JOGADOR  {jogadores[individual]["nome"]}: ')
            for i, v in enumerate(jogadores[individual]['gols']):
                print(f'    No jogo {i} fez {v} gols.')
print()
print('<<<< OBRIGADO POR NOS USAR, VOLTE SEMPRE >>>>')
