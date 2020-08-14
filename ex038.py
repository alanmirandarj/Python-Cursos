#um programa que leia dois numeros e fale qual e o maior ou se são iguais
n1 = int(input('Primeiro numero : '))
n2 = int(input('Segundo numero : '))
if n1>n2:
    print('O primeiro numero é maior')
elif n1<n2:
    print('O segundo numero é maior')
elif n1==n2:
    print('Os dois numeros são iguais')
else:
    print('Digite os numeros corretamente!')
