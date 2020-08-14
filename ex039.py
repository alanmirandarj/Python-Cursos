#faca um programa que leia  ano de nascimento do candidato e veja se ele ainda vai se a
# lista se ele ja se alistou ou se ele tem que se alistar deve mostrar o tempo que faltaq ou que passou do prazo
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade<18:
    saldo = 18 - idade
    print('você não tem 18 anos ainda falta {} anos para o alistamento '.format(saldo))
elif idade==18:
    print('Você deve se alista imediatamente !!')
else:
    saldo = idade - 18
    print('Você não precisa se alistar , seu alistamento foi em {} anos atras'.format(saldo))
