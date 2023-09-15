def voto(nascimento):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - nascimento
    votar = ''
    if idade < 16:
        votar = f'Com {idade} anos: Não pode votar!'
        return votar
    elif 18 <= idade < 65:
        votar = f'Com {idade} anos: Voto obrigatório!'
        return votar
    else:
        votar = f'Com {idade} anos: Voto optativo!'
        return votar


# Programa principal
anoNascimento = int(input('Qual seu ano de nascimento: '))
print(f'{voto(anoNascimento)}')
