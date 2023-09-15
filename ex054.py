c1 = 0
c2 = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        c1 = peso
        c2 = peso
    else:
        if peso > c1:
            c1 = peso
        if peso < c2:
            c2 = peso
print('O maior peso foi de {:.0f}Kg, o menor peso foi de {:.0f}Kg.'.format(c1, c2))