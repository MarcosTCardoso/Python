num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    user = int(input('Digite um número de 0 a 20: '))
    if 0 <= user <= 20:
        print(f'{user}: {num[user]}.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        while continuar not in 'SsNn':
            continuar = str(input('Opção inválida. Quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'N':
            break



