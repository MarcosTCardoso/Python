nomes = {}
nomes['nome'] = str(input('Nome: '))
nomes['media'] = float(input(f'Média de {nomes["nome"]}: '))
if nomes['media'] >= 7:
    nomes['situação'] = 'Aluno aprovado!'
elif 5 <= nomes['media'] > 7:
    nomes['situação'] = 'Aluno em recuperação!'
else:
    nomes['situação'] = 'Aluno reprovado!'
print('-=' * 30)
for i, v in nomes.items():
    print(f'  - {i} é {v}')
