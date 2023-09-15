'''#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#for comida in lanche:
#    print(f'Eu vou comer {comida}.')
#print('Comi pra caramba!')
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}.')
    #Se eu não precisar da posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
#se eu precisar da posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
#também me da a posição
print(sorted(lanche))'''
import random
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
