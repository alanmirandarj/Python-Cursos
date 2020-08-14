numero = list()

while True:
    valor = int(input('Digite um valor :'))
    if valor not in numero:
        numero.append(valor)
        
    else:
        print('+==+==+==   Valor duplicado !  Não vou adicionar ... ==+==+==+===' )


    print('Adicionado com sucesso ....')

    n = str(input('Deseja continuar ? S/N' ))
    print('=+='*30)
    if n in 'Nn':
        break
numero.sort()
print(f'Os numeros digitados foram {numero}')    
        
    
