'''palavras = ('Cabelo', 'Diana', 'Amanda', 'Cavalo', 'Padrinho', 'Mesquita', 'Padre')
for i in palavras:
    print(f'Na palavra {i}, temos ', end='')
    if 'a' in i:
        print('a', end=' ')
    if 'e' in i:
        print('e', end=' ')
    if 'i' in i:
        print('i', end=' ')
    if 'o' in i:
        print('o', end=' ')
    if 'u' in i:
        print('u', end=' ')
    print('.\n')'''
palavras = ('Cabelo', 'Diana', 'Amanda', 'Cavalo', 'Padrinho', 'Mesquita', 'Padre')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')

