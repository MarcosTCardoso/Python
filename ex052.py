'''frase = str(input('Digite um frase para saber se é um palíndromo: ')).strip().lower()
c1 = frase.split()
c2 = ''.join(c1)
c3 = c2[::-1]
print('O inverso de {} é {}.'.format(frase, c3))
if c2 == c3:
    print('A frase ({}) é considerada um palíndromo.'.format(frase))
else:
    print('A frase ({}) não é considerada um palíndromo.'.format(frase))'''
frase = str(input('Digite uma frase: ')).strip().lower()
c2 = frase.split()
c3 = ''.join(c2)
inv = ''
for c in range(len(c3) -1, -1, -1):
    inv += c3[c]
print('A frase digitada foi {}, seu inverso é {}.'.format(frase, inv))
if inv == c3:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')