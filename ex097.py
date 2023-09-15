def escreva(msg):
    print('~' * (len(msg) + 6))
    print(f'   {msg}   ')
    print('~' * (len(msg) + 6))


escreva(str(input('Digite o título: ')))
