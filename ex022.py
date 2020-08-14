nome = str(input('Digite seu nome completo : ')).strip()
print('Analisando seu nome ...'.format())
print('Seu nome em maiuscula é {} '.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))#calcula o espaço e as quantidades de letras sem ele
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))#quantidade apenas do primeiro nome

