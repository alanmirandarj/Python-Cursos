s = 0
c = 0
for i in range(1, 7):
    num = int(input('Digite o {}° valor :'.format(i)))
    if num % 2 ==0:
        s += num
        c += 1
print('Você informou {} pares numero e a soma foi {}'.format(c,s))
