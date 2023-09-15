from math import sqrt
alt = float(input('Qual sua altura? '))
pes = float(input('Qual seu peso? '))
imc = pes / (alt * alt)
if imc < 18.5:
    print('Você está abaixo do peso recomendado. ')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal. ')
elif imc >=25 and imc < 30:
    print('Você está com sobrepeso. ')
elif imc >=35 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida. ')
print('Seu IMC é de {:.1f}.'.format(imc))