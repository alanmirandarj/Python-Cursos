tot = 0
n1 = int(input('Digite um numero :'))
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('O numero {} foi divisivel {} vezes '.format(n1, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
