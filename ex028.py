from random import randint#randit sorteia os numeros
from time import sleep
print('-=-' *20)
print('Vou pensar em um numero de 0 a 5 tente adivinhar')
print('-=-' *20)#faz uma lista na tela
escolhido = randint(0,5)#faz o pc adivinhar um numero
n = int(input('Advinhe o numéro de 0 a 5 que estou pensando : '))
print('PROCESSANDO...')
sleep(2)#o comando sleep do time simula um tempo de processamento
if n == escolhido:
    print("Parabéns seu numero foi {} voce acertou".format(n))
else:
    print('Infelizmente você não acertou o nomero escolhido foi {}, '.format(escolhido))

#import random
#from time import sleep
#print(' A maquina irá pensar em um número de 0 a 5,\n'
 #     ' você deverá acertar qual foi esse número.')
#n=int(input('digite um número de 0 a 5: '))
#print('PROCESSANDO. . .')
#sleep(2)
#valores=(0,1,2,3,4,5)
#escolhido=random.choice(valores)
#if n==escolhido: print("Parabéns, você acertou")
#else: print("Que pena, você errou, o número escolhido pela máquina foi {}".format(escolhido))


