from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
hoje = date.today().year
dados['idade'] = hoje - nascimento
ctps = int(input('Digite o número da CTPS: (0 se não for assinada): '))
if ctps != 0:
    dados['ctps'] = ctps
    dados['Contratação'] = int(input('Qual o ano de contratação? '))
    dados['salário'] = float(input('Qual o salário? R$ '))
    dados['aposentadoria'] = (dados['Contratação'] + 35) - nascimento
print('-='*30)
for i, v in dados.items():
    print(f'{i} tem o valor {v}')