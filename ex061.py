'''refarça o 51 mostrando os 10 primeiro termo da razao pa '''
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
t1 = int(input('Primeiro termo :'))
r1 = int(input('Qual a razão:'))
termo = t1
c = 1
while c <= 10:
     print('{} - '.format(termo), end=' =>')
     termo+=r1
     c += 1
print('ACABOU !!!')
