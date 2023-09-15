from datetime import date
s1 = 0
s2 = 0
year = date.today().year
s3 = year - 18
for s in range(0, 7):
    idade = int(input('Digite o ano de nascimento: '))
    if idade > s3:
        s1 = s1 + 1
    else:
        s2 = s2 + 1
print('{} pessoas são maiores de idade e {} são menores de idade.'.format(s2, s1))
