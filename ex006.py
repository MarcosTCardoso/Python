import random
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))
m = (n1 + n2 + n3 + n4)/4
c = random.randint(1000,10000)
if m < 6:
    print('Você ficou de recuperação.')
else:
    print('Parabéns, você está aprovado.')
if m >= 9:
    print('Você é um aluno excepcional informe o seguinte código ao seu professor {}.'.format(c))
print('A sua média é de {}.'.format(m))
