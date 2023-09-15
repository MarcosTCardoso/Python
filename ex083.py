dados = list()
controlador = 0
while True:
    express = str(input('Digite sua expressão: '))
    for a in express:
        if a == '(':
            controlador += 1
        elif a == ')':
            controlador -=1
    if controlador == 0:
        print('Sua expressão é válida!')
        break
    if controlador != 0:
        print('Sua expressão é inválida!')
        break
