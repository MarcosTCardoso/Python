'''def titulo(txt):
    print('-' * 60)
    print(txt)
    print('-' * 60)
titulo(f'{"Curso em vídeo":^60}')
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
# Programa Principal
soma(3, 5)
soma(b=int(input('Digite um número: ')), a=int(input('Digite o segundo número: ')))
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e seu tamanho é {tam}.')
contador(2, 5, 7, 9)
contador(3, 2, 5)
contador(2, 1)'''


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [0, 15, 12, 11]
dobra(valores)
print(valores)
