from datetime import date
idade = int(input('Qual o ano de nascimento do atleta? '))
yeara = date.today().year
midade = yeara - idade
if midade <= 9:
    print('Esse é um atleta MIRIM. ')
elif midade <= 14:
    print('Esse é um atleta INFANTIL. ')
elif midade <= 19:
    print('Esse é um atleta JÚNIOR. ')
elif midade <= 20:
    print('Esse é um atleta SÊNIOR. ')
else:
    print('Esse é um atleta MASTER. ')
print(midade)