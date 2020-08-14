# jokenpo pedra papel tesoura faca o pc jogar com vc
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
escolha = int(input(''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

print('-=-' * 20)
print('O computador escolheu {} '.format(itens[computador]))

print("O jogador escolheu {} ".format(itens[escolha]))
print('-=-' * 20)
if computador == 0:
    if escolha == 0:
        print('Empatou !!')
    elif escolha == 1:
        print('Você ganhou !!')
    elif escolha == 2:
        print('O computador ganhou !!')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if escolha == 0:
        print('O computador ganhou !!')
    elif escolha == 1:
        print('Empatou !!')
    elif escolha == 2:
        print('Você ganhou !!')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if escolha == 0:
        print('Você ganhou !!')
    elif escolha == 1:
        print('O computador ganhou !!')
    elif escolha == 2:
        print('Empatou !!')
    else:
        print('Jogada Invalida')
