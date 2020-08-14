from random import randint
v =0
print('--=--'*30)
print('Vamos Jogar Par ou Ímpar ?')
print('--=--'*30)
while True:
    jogador = int(input('Digite um valor :'))
    pc=randint(0,10)
    total = pc + jogador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar ?[P]/[I]')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total} DEU ',end='')
    print('PAR'if total % 2 == 0 else 'IMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você venceu !!!')
            v+=1
        else:
            print('Você perdeu !!')
            break
    elif tipo =='I':
        if total % 2 ==1:
            print('Você venceu !!!')
            v+=1
        else:
            print('Você perdeu !!')
            break
    print('Vamos jogar novamente ?')
print(f'GAME OVER !!você venceu {v} vezes')
