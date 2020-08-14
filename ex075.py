'''desenvolva um programa que leia quatro nuemros no teclado e guardeos em uma
tupla e mostreo no final.
digite um numero x 4
voce digitou os valores (????)
o valor 9 apareceu {} vez
o valor 3 apareceu na posicao {}
os valores pares digitados foram {} '''
n1 =(int(input('Digite um numero : ')),
     int(input('Digite um numero : ')),
     int(input('Digite um numero : ')),
     int(input('Digite um numero : ')))

print(f'Você digitou os valores {n1} .')
print(f'O valor {n1[0]} apareceu {n1.count(n1[0])} vezes')
print(f'O valor {n1[3]} apareceu na 4ª posição ')
print('Os valores pares digitados foram',end=' ')
for n in n1:
 if n % 2 == 0:
  print(f' {n}',end=' ')

