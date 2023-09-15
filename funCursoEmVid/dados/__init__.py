
def leiaDinheiro(msg):
    válido = False
    while not válido:
        d = str(input(msg)).replace(',', '.').strip()
        if d.isalpha() or d == '':
            print(f'\033[0;31mERRO! \"{d}\" não é considerado um preço válido.\033[m')
        else:
            válido = True
            return float(d)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('O número digitado não é um inteiro.')
            continue
        except KeyboardInterrupt:
            print('O usuário não quis informar os dados solicitados.')
            return 0
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('O número digitado não é real.')
        except KeyboardInterrupt:
            print('O usuário não quis informar os dados solicitados.')
            return 0
        else:
            return n
                





#def leiaFloat(num):
