fra = str(input('Digite uma frase: ')).strip().upper()
print('A letra (a) aparece {} vezes na frase.'.format(fra.count('A')))
print('A letra (a) inicia na casa {} na frase.'.format(fra.find('A')+1))
print('A útima letra (a) aparece na casa {} na frase.'.format(fra.rfind('A')+1))