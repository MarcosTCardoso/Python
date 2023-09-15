from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
resultado = 0
conta = False
while not conta:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    operacao = int(input('Qual operação deseja realizar? '))
    if operacao == 1:
        resultado = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, resultado))
    elif operacao == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, resultado))
    elif operacao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre o valor {} e o valor {} o maior é o {}.'.format(n1, n2, maior))
    elif operacao == 4:
        print('Digite os valores novamente: ')
        n1 = int(input('Qual o novo primeiro número? '))
        n2 = int(input('Qual o novo segundo número? '))
    elif operacao == 5:
        print('Finalizando...')
        sleep(3)
        print('Obrigado por usar nosso programa.')
        print('-=-' * 10)
        conta = True
    else:
        print('Opção inválida.')
        