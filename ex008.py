vel = float(input('Digite a velocidade que o veículo passou no radar: '))
valv = 80
if vel <= 80:
    print('O motorista não foi multado!')
else:
    print('O motorista foi multado no valor de R$ {:.2f}.'.format((vel - valv)*7))