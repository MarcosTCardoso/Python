nome = str(input('Qual o seu nome? ')).strip().title()
nomec = nome.split()
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer {}{}{}.'.format(cores['pretoebranco'], nomec[0], cores['limpa']))
