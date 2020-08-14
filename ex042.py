#complemewntar o desaf 35 : se ele puder formar o triangulo informar se e
# equilatero = se tiver 3 lados iguais, isoselos se apenas 2 lados forem iguais , e escalenos se todos forem difernte
print('-=-' *20 )
print(' =-=-=-=-=-=-=  Analisador de triangulos   =-=-=-=-=-=-==')
print('-=-' *20 )
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))
if a+b >c and c+b > a and c+a > b:
    if a == b == c:
        print('Os seguimentos informados ', end='')
        print('formar um triangulo é equilatero ')
    elif a != b !=c != a:
        print('formar um triangulo é escaleno')
    else:
        print('formar um triangulo é isoceles')
else:
    print('não pode formar um triangulo')

