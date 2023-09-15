def contador(ti, tf, ra):
    while True:
        back = 0
        if ra > 0 and ti < tf:
            pro = ti
            print(f'{ti} ', end='')
            while True:
                pro += ra
                if pro > tf:
                    break
                print(f'{pro} ', end='')
                back = 1
        if ra == 0:
            na = ra + 1
            pro = ti
            print(f'{ti} ', end='')
            while True:
                pro += na
                if pro > tf:
                    break
                print(f'{pro} ', end='')
                back = 1
        elif ti > tf:
            if ra < 0:
                pro = ti
                print(f'{ti} ', end='')
                while True:
                    pro = pro - (-ra)
                    if pro < tf:
                        break
                    print(f'{pro} ', end='')
                    back = 1
            if ra > 0:
                pro = ti
                print(f'{ti} ', end='')
                while True:
                    pro = pro - ra
                    if pro < tf:
                        break
                    print(f'{pro} ', end='')
                    back = 1
            if ra == 0:
                na = ra + 1
                pro = ti
                print(f'{ti} ', end='')
                while True:
                    pro += na
                    if pro > tf:
                        break
                    print(f'{pro} ', end='')
                    back = 1
        if back == 1:
            break
    print('FIM')


def linha():
    print('-=' * 30)


linha()
print('Vamos contar de 1 a 10, com a razão 1.')
contador(1, 10, 1)
linha()
print('Vamos contar de 10 a 1, com razão -1.')
contador(ti=10, tf=1, ra=-1)
linha()
print('Agora é a sua vez de escolher:')
contador(ti=int(input('início: ')), tf=int(input('Fim: ')), ra=int(input('Razão: ')))

