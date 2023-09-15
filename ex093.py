aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
aproveitamento['gols'] = list()
for j in range(1, jogos + 1):
    gol = int(input(f'Quantos gols na partida {j}? '))
    aproveitamento["gols"].append(gol)
aproveitamento['total'] = sum(aproveitamento['gols'])
print('-=' * 30)
print(aproveitamento)
print('-='*30)
for i, v in aproveitamento.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {jogos} partidas.')
for i, a in enumerate(aproveitamento["gols"]):
    print(f'    ==> Na partida {i + 1}, fez {a} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
