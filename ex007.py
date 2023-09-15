'''from random import randint
num = randint(0,5)
chute = int(input('Chute um número de 0 a 5: '))
Valor = True
while Valor == True:
    if chute > 5:
        print('Você não pode chutar esse número, chute outro: ')
        chute = int(input('Digite seu novo chute: '))
    elif chute > num:
        print('O número é menor que esse, tente novamente: ')
        chute = int(input('Digite seu novo chute: '))
    elif chute < num:
        print('O número é maior que esse, tente novamente: ')
        chute = int(input('Digite seu novo chute: '))
    elif chute == num:
        print('Parabéns, você acertou!')
        Valor = False
print('O número correto era o {}.'.format(num)'''
from random import randint
from time import sleep
comp = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar se puder.')
print('-=-' * 20)
chute = int(input('Chute um número de 0 a 5! '))
print('Processando...')
sleep(2)
if chute == comp:
    print('Parabéns, você me venceu!')
else:
    print('Você não é páreo para meu poder mortal, sucumba.')