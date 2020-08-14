print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
t1 = int(input('Primeiro termo :'))
r1 = int(input('Qual a razão:'))
dec = t1 + (10 - 1) * r1
for s in range(t1, dec+r1, r1):
    print('{}'.format(s), end=' =>')
print('ACABOU !!!')
