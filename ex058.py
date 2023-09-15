'''from random import randint
computer = randint(1, 11)
user = 0
palpite = 0
while palpite == 0:
    chute = int(input('Qual seu palpite? '))
    user += 1
    if chute == computer:
        print('Parabéns, você acertou.\n Para isso você chutou {} vezes.'.format(user))
        palpite = 1
    else:
        print('Você errou.')'''
from random import randint
computador = randint(1, 10)
print('Sou seu computador, vou pensar em um número de 1 a 10...')
print('Será que você consegue acertar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('O número é menor.')
        if jogador < computador:
            print('O número é maior.')
print('Acertou com {} testativas! Parabéns.'.format(palpite))