#crie um programa que tenha uma tupla com vinte numeros por extenso:
# digite um numero entre 0 e 20 , voce gitou o nuemro dez fim, opção invalida digite um numero novament
lista = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinza','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
  n = int(input('Digite um numero entre 0 e 20 :'))
  if 0 <= n <= 20:
      break
  print('Tente novamente ', end='')
n = lista[n]
print(f'O numero que digitou foi o {n}')




