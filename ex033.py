a = int(input('Digite o primeiro valor desejado :'))
b = int(input('Digite o segundo valor desejado :'))
c = int(input('Digite o terceiro valor desejado :'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c


print('O menor valor ditado foi {}\nO maior valor ditado é {}  '.format(menor,maior))



