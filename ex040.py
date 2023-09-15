'''n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))
md = (n1 + n2) / 2
if md < 5:
    print('Você está reprovado!')
elif md >= 5 and md <7:
    print('Você está de recuperação!')
else:
    print('Parabéns, você está aprovado!')'''
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno?'))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno fica em {}.'.format(n1, n2, media))
if 7 > media <= 5:
    print('Você está de RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')

