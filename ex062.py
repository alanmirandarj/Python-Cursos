'''melhore o desafio 61 perguntando se ele quer mostrar mais termo'''
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
t1 = int(input('Primeiro termo :'))
r1 = int(input('Qual a razão:'))
termo = t1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
            termo += r1
            c += 1
            print('{} - '.format(termo), end=' =>')
    print('PAUSA !!!')
    mais = int(input('Deseja adionar mais quantos ? '))
print('Progreção finalizada com {}  termos '.format(total))


