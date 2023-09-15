from time import sleep
import emoji
for c in range(10, -1, -1):
    print('\033[31m{}\033[m'.format(c))
    sleep(1)
print('BOOM! BOOM! POW!')
print(emoji.demojize(":thumbs_up:", language='alias'))
