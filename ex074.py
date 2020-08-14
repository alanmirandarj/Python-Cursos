'''crie um progrma que vai gerar 5 numeros aleadtorio e guardar em uma tupla
depois mostra a listagem dos numeros gerados mostre o maior e o menor numero que estao na tupla
o valor sorteado foi
o menor valor sorteado foi
o maior valor sorteado foi'''
from random import randint
n = (randint(1,60),randint(1,60),randint(1,60)
     ,randint(1,60),randint(1,60))
print(f'Eu sortiei os valores {n} ',end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
