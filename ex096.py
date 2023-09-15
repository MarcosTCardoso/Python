'''def terreno(a, b):
    area = a * b
    print(f'A área de um terreno {a} X {b} é de {area}m².')


terreno(float(input('Largura (m): ')), float(input('Comprimento (m): ')))'''


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é {a}m²')



print('CONTROLE DE TERRENOS')
print('-=' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)