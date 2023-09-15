cat1 = float(input('Qual o valor da primeira reta? '))
cat2 = float(input('Qual o valor da segunda reta? '))
hip = float(input('Qual o valor da terceira reta? '))
'''x = cat1 + cat2
l = cat2 + hip
r = hip + cat1
if x < hip or l < cat1 or r < cat2:'''
if cat1 + cat2 <= hip or cat2 + hip <= cat1 or hip + cat1 <= cat2:
    print('Não é possível fazer um triângulo com essas medidas.')
else:
    print('É possível fazer um triângulo com essas medidas.')
'''if l < cat1:
    print('Não é possível fazer um triângulo com essas medidas.')
else:
    print('É possível fazer um triângulo com essas medidas.')
if r < cat2:
    print('Não é possível fazer um triângulo com essas medidas.')
else:
    print('É possível fazer um triângulo com essas medidas.')'''
