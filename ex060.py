'''numero que mostre o fatorial do numero'''
'''from math import factorial
n = int(input('Digite um numero para calcular o fatorial : '))
f = factorial(n)
print('O fatoria de {} é {} '.format(n, f))
'''
from math import factorial
n = int(input('Digite um numero para calcular o fatorial : '))
f = factorial(n)
c = n
f = 1
print('calculando o fatorial de {} =  '.format(n),end='')
while c > 0:
    print(' {} '.format(c),end='')
    print('x'if c>1 else '=',end='')
    f*=c
    c-=1
print('{} '.format(f))
