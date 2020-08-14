
numero = int(input('Digite um numero para converte-lo :'))
print('-=-'*20)

print('Digite :')
print('''
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Escolha uma opção :'))

print('-=-'*20)
if opcao == 1:
    print('{} Convertido para Binário é igual {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print(('{} Convertido para Octal é igual a {} '.format(numero, oct(numero)[2:])))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual {} '.format(numero,hex(numero)[2:]))
else:
    print('Opção incorreta, digite novamente ')