'''melhore o desafio 028 que nao pare de tentar ate adivinhar e conte as vezes que tentou'''
from random import randint  # randit sorteia os numeros
from time import sleep

print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5 tente adivinhar')
print('-=-' * 20)  # faz uma lista na tela
escolhido = randint(0, 5)  # faz o pc adivinhar um numero
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Advinhe o numéro de 0 a 5 que estou pensando : '))
    palpite += 1

    print('PROCESSANDO...')
    sleep(0.5)  # o comando sleep do time simula um tempo de processamento
    if escolhido == jogador:
        acertou = True

        print('-=-'*30)

        print("Parabéns seu numero foi {} voce acertou com {} tentativas".format(escolhido, palpite))
    else:
        if jogador > escolhido:
            print('Tente um numero menor')

        elif jogador < escolhido:

            print('Tente um numero maior')

        print('Infelizmente você não acertou tente novamente , ')
