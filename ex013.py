sal = float(input('Qual o salário do seu funcionário? '))
salm = 1250
sala = 0
if sal > salm:
    sala = sal + sal * 0.10
else:
    sala = sal + sal * 0.15
print(sala)