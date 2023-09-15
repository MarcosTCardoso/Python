from time import sleep


def maior(* num):
    linha()
    print('Analisando os valores passados...')
    for a in num:
        print(f'{a} ', end='')
        sleep(0.25)
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior número é {max(num)}.')


def linha():
    print('-'*60)


maior(1, 5, 10, 3, 20)
maior(0)