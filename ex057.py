''''Faça o programa que peça para informar o sexo da pessoa com opcao f/
m e so aceite m / f caso esteja errado pedi novamnte'''
sexo = str(input('Digite seu sexo [M]/[F]: ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('sexo digitado invalido digite novamente :')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))


