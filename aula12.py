nome = str(input('Qual é o seu nome? '))
if nome == 'Marcos':
    print('Você tem um belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Claudia Jessica Juliana Pri':
    print('Seu nome feminino é bem popular no Brasil.')
print('Tenha um bom dia, {}!'.format(nome))
