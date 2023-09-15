vlc = float(input('Qual o valor do imóvel que deseja comprar? '))
sal = float(input('Qual seu salário mensal? '))
time = float(input('Em quantos anos vai pagar esse imóvel? '))
prest = vlc/(time*12)
imps = (prest * 100) / sal
prestj = prest + prest * 0.15
if imps >= 30:
    print('Seu empréstimo não foi autorizado, tente com um período maior. ')
elif imps < 30:
    print('Seu empréstimo foi autorizado.\nO valor da sua parcela é de \033[31m R$ {:.2f}\033[m.'.format(prestj))