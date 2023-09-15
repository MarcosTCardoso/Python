'''
import random
from random import randint

aluno = ['Pedro', 'João', 'José', 'Maria']
alunos = False
while alunos == False:
    aluno1 = random.randint(0, 3)
    aluno2 = random.randint(0, 3)
    aluno3 = random.randint(0, 3)
    aluno4 = random.randint(0, 3)
    if aluno2 == aluno1:
        aluno2 = random.randint(0, 3)
    elif aluno3 == aluno2:
        aluno3 = random.randint(0, 3)
    elif aluno3 == aluno1:
        aluno3 = random.randint(0, 3)
    elif aluno4 == aluno3:
        aluno4 = random.randint(0, 3)
    elif aluno4 == aluno2:
        aluno4 = random.randint(0, 3)
    elif aluno4 == aluno1:
        aluno4 = random.randint(0, 3)
    elif aluno1 != aluno2 and aluno1 != aluno3 and aluno1 != aluno4 and aluno2 != aluno3 and aluno2 != aluno4 and aluno3 != aluno4:
        alunos = True

print(aluno[aluno1], aluno[aluno2], aluno[aluno3], aluno[aluno4])
'''
import random
n1 = str(input('Qual o primeiro aluno? '))
n2 = str(input('Qual o segundo aluno? '))
n3 = str(input('Qual o terceiro aluno? '))
n4 = str(input('Qual o quarto aluno? '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print("A ordem dos alunos sera {}.".format(alunos))