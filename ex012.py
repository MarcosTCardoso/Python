'''num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
numa = num1 % 3
numx = 0
numz = 0
if num1 <= num2 and num1 <= num3:
    numx = num1
if num2 <= num1 and num2 <= num3:
    numx = num2
if num3 <= num1 and num3 <= num2:
    numx = num3
if num1 >= num2 and num1 >= num3:
    numz = num1
if num2 >= num1 and num2 >= num3:
    numz = num2
if num3 >= num1 and num3 >= num2:
    numz = num3
print('O menor número é {} e o maior número é {}.'.format(numx, numz))'''

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
numa = [num1, num2, num3]
numm = max(numa)
numn = min(numa)
print('o min é {} e o max é {}.'.format(numn, numm))