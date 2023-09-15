pt = int(input('Digite o primeiro termo da progressão aritmética: '))
ra = int(input('Digite a razão da progressão aritmética: '))
tf = pt + ra * 10
xa = 0
for c in range(pt, tf, ra):
    xa = list(range(pt, tf, ra))
    print(c, end=' -> ')

