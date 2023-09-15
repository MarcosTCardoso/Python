def ficha(nome='<desconhecido>', gols=''):
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


jogador = str(input('Qual o nome do jogador? '))
gol = str(input('Quantos gols ele fez no campeonato? '))
pontos = ''
if gol.isnumeric():
    pontos = gol
ficha(jogador, pontos)
