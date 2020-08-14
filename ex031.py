distancia = int(input('Qual a distancia da viagem ? '))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Você esta presta a começar a viagem de {} KM, e o preco da sua viagem é R$ {:.2f}'.format(distancia, valor))


""""'''valor2 = distancia * 0.500
if distancia >= 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50
print('Você esta presta a começar a viagem de {} KM, e o preco da sua viagem é R$ {:.2f}'.format(distancia, valor))''''''

"""