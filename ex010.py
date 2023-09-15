dis = float(input('Qual a distância do seu destino: '))
'''da pra fazer da seguinte forma:
preco = dis * 0.5 if dis > 200 else: dis * 0.45'''
if dis <= 200:
    print('A tarifa para viagens de até 200KM é de R$ 0,50 por KM. \nO preço da sua passagem é de R$ {}.'.format(dis * 0.5))
else:
    print('A tarifa para viagens de mais de 200KM é de R$ 0,45 por KM. \nO preço da sua passagem é de R$ {}.'.format(dis * 0.45))