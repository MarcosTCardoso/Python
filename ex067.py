while True:
    num = int(input('Digite o número que deseja ver a tabuada: '))
    if num < 0:
        break
    print('=-=' * 20)
    for tabuada in range(1, 11):
        result = num * tabuada
        print(f'{num} X {tabuada} = {result}')
    print('=-='*20)
print('Programa Tabuada encerrado! \nVolte sempre.')