import math
grau = int(input('Qual o angulo você deseja calcular? '))
sen = math.sin(grau)
cos = math.cos(grau)
tang = math.tan(grau)
print('O seno de {} é {:.2f}.'.format(grau, sen))
print('o cosseno de {} é {:.2f}.'.format(grau, cos))
print('A tangente de {} é {:.2f}.'.format(grau, tang))