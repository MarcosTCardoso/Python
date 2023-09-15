'''r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Você não pode ter um triângulo com essas medidas. ')
elif r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('Você pode ter um triângulo com essas medidas. ')
    if r1 == r2 and r1 == r3:
        print('Esse é um triangulo equilátero.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esse é um triângulo escaleno.')
    else:
        print('Esse é um triangulo isósceles.')'''
r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanhno da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você pode formar um triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES!')
else:
    print('Não se pode ter um triângulo com essas medidas.')