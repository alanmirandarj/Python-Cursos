'''faca um programa que  leia dois valores e leia um menu somar/multiplicar/ma
ior /novos numeros/ sair do programa'''
#n = 0
#while not 0:
from time import sleep
n1 = int(input('Digite o primeiro numero : '))
print('=-=' * 20)
n2 = int(input('Digite o segundo numero :'))
print('=-=' * 20)

es=0
while es != 5:
    print('=-=' * 20)

    es = int(input('Escolha no menu abaixo as opções : ' '\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair \n '))
    if es == 1:
        soma = n1 + n2
        print('A soma de {} + {} é = {} '.format(n1, n2, soma))
    elif es == 2:
        mult = n1 * n2
        print('A multiplicação de {} x {} é = {} '.format(n1, n2, mult))
    elif es == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior numero é {}'.format(n1, n2, maior))
    elif es == 4:
        print('informe os numeros denovo :')
        n1 = int(input('Digite o primeiro numero : '))
        n2 = int(input('Digite o segundo numero :'))
        print('=-='*20)
    elif es == 5:
        print('Finalizando.')
        sleep(1.5)

        print('.')
    else:
        print('Digite uma opção valida !!')
        print('=-='*20)

print('Fim do programa!!')
print('=-=' * 20)
