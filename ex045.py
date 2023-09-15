'''from random import randint
import emoji
print('\033[31m-=-\033[m' * 20)
print('{:^60}'.format('Bem-vindo ao JOKENPÔ'))
print('\033[31m-=-\033[m' * 20)
game = randint(0,2)
jok = 0
chute = str(input('Chute entre pedra, papel ou tesoura: '))
if game == 1:
    jok = jok + 1
elif game == 2:
    jok = jok + 2
if jok == 0:
    print('O computador escolheu PEDRA.')
elif jok == 1:
    print('O computador escolheu PAPEL.')
elif jok == 2:
    print('O computador escolheu TESOURA.')
g1 = 0
if chute == 'pedra':
    g1 = g1 + 0
elif chute == 'papel':
    g1 = g1 + 1
elif chute == 'tesoura':
    g1 = g1 + 2
if jok == g1:
    print('Vocês empataram.')
elif jok == 0 and g1 == 1:
    print('Parabéns, você venceu.')
elif jok == 0 and g1 == 2:
    print('Que pena, você perdeu.')
elif jok == 1 and g1 == 0:
    print('Que pena, você perdeu.')
elif jok == 1 and g1 == 2:
    print('Parabéns, você venceu.')
elif jok == 2 and g1 == 0:
    print('Que pena, você perdeu.')
elif jok == 2 and g1 == 1:
    print('Parabéns, você venceu.')'''
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('''Para jogar escolha uma das opções abaixo:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 10)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('empate.')
    elif jogador == 1:
        print('jogador venceu.')
    elif jogador == 2:
        print('computador venceu.')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('empate.')
    elif jogador == 2:
        print('jogador venceu.')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('jogador venceu.')
    elif jogador == 1:
        print('jogador perdeu.')
    elif jogador == 2:
        print('empate.')
    else:
        print('Jogada inválida!')