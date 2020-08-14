print('-=-' *20 )
print(' =-=-=-=-=-=-=  Analisador de triangulos   =-=-=-=-=-=-==')
print('-=-' *20 )
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))
if a+b >c and c+b > a and c+a > b:
    resultado = 'pode'
else:
    resultado = 'não pode'
print('Os seguimentos informados {} formar um triangulo'.format(resultado))
